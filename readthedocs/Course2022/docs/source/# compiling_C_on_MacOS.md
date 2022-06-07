# Compiling and linking with c-files on MaxOS

## Problems:

Compilation and linking troubles on MaxOS, because Apple changed oridnary locations for include files and change the way the dynamic libarries are to be linked:

    * no stdlib.h and stdio.h in /usr/include
	* no direct access to dynamic libraries; you must now use the `dynamic library cache`.

Therefore Pymake is no longer up-to-date and we have to alter the makefile that our programs by hand to get the compiling and linking done.

## Compiling, the incude files

First make sure that the include files are found by softlinking them to the standard directory where they are normallly searched

The coarse method is (which I did) by typing in terminal:

    $ sudo ln -s /Library/Developer/CommandLineTools/SDKs/MacOSX11.1.sdk/usr/include/*.h /usr/local/include

However, this may be a better (more hygienic way) to achieve the same effect by typing in terminal:

    $ export CPATH=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/

Then show the new softlink by typling in terminal:

    $ ls -sla /usr/local/include/stdio.h

to get

    0 lrwxr-xr-x  1 root  wheel  75 Nov  1  2021 /usr/local/include/stdio.h -> /Library/Developer/CommandLineTools/SDKs/MacOSX11.1.sdk/usr/include/stdio.h

which shows the created softlink from `/usr/loca/bin` to the deeply burried `include` files

## Linking, using the dynamic link cache

To use the dynamic link cache, we first have to find out where it is. A command-line session showing how to find it is here

    https://developer.apple.com/forums/thread/669094

Following this session partly:

Make a small test c-program, here shown using `cat` in terminal

    $ cat test.c
    #include <unistd.h>
    const unsigned char pmessagebuf[13] = "hello world\n";
    int main (int argc, char* argv[])
    {
    write(STDOUT_FILENO, (void*)pmessagebuf, 12);
    return(0);
    }

Compiling and linke can be done automatically

    $ cc test.c -o test

and then the program text can be run

    $ ./test
    hello world

TO see what's happening behind the screens, add the -v (--verbose) option and recompile

    $ cc test.o -o test --verbose

This spits out a lot of information, among which the full line of the call to the linker (ld)

    "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld" -demangle -lto_library /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/libLTO.dylib -no_deduplicate -dynamic -arch x86_64 -platform_version macos 12.0.0 12.3 -syslibroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -o test -L/usr/local/lib /var/folders/90/m51x_b713y561gzh2kzy18d00000gq/T/test-b03556.o -lSystem /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/13.1.6/lib/darwin/libclang_rt.osx.a

In is line is the following option:

    -syslibroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk

which is the system cache

So to make your own make file work, define a parameter to hold this sysroot like so

    sysroot=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk

and add `-syslibroot==$sysroot` to the line in hte make file that constructs your program (with the linker).

Note: in `gortran`, the option use `-sysroot=$sysroot` not `-syslibroot`.

In your makefile this may look like this (here I am compiling the program modflow 2005):

    mf2005: $(OBJECTS)
        -$(F90) $(F90FLAGS) -o $(PROGRAM) --sysroot $(SYSLIBROOT) $(OBJECTS) $(SYSLIBS) -I$(OBJDIR) -J$(OBJDIR) 

and type

    $ make all

in the terminal
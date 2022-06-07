===========================
Previous exams with answers
===========================

:Author: Prof. dr.ir. T.N.Olsthoorn

Open-book exam (1h), Feb 7, 2022
================================

Question 1
----------

Questions 1.1 and 1.2

A well is installed at 250 m distance from a river. The well fully penetrates the aquifer. The aquifer is unconfined, it has a conductivity of k= 30 m/d and a representative thickness of 40 m, which may be assumed constant. It further has a storage coefficient (specific yield) of S=0.20. The well extracts water at a rate of *Q*\ =1200 m\ :sup:`3`/d during exactly 7 days, after which it stops. The questions refer to the drawdown in point p at 50 m from the well on the line through the well perpendicular to the river as shown in the figure.

.. container:: centering

   .. figure:: pictures/2022_1.png
      :alt: Well adjacent to a straight fully penetrating river. The aquifer is homogeneous and extends to infinity.This is clearly a well in an aquifer with constant transmissivity, for which the well-known Theis solution is applicable. To obtain values for the Theis well function, you can make use of the Theis type curve shown below.
      :width: 80.0%

      Well adjacent to a straight fully penetrating river. The aquifer is homogeneous and extends to infinity.This is clearly a well in an aquifer with constant transmissivity, for which the well-known Theis solution is applicable. To obtain values for the Theis well function, you can make use of the Theis type curve shown below.

.. container:: centering

   .. figure:: pictures/2022_2.png
      :alt: Theis type curve, i.e., the Theis well function as a function of :math:`1/u`
      :width: 80.0%

      Theis type curve, i.e., the Theis well function as a function of :math:`1/u`

#. What will be the drawdown at point p at :math:`t=7` d after the start of the extraction?

--------------

Generalities:

The transient drawdown due to a well in an aquifer of constant transmissivity extracting at a constant rate from :math:`t=0` is according to the Theis solution

.. math:: s(r,t)=\frac{Q}{4\pi\text{kD}}\mathrm{W}(u)\mbox{, with }u=\frac{r^{2}S}{4kDt}

But we must take care of the river, which creates a fixed-head boundary condition. This is done by placing a mirror well of opposite sign at the exact opposite side of the river and at the same distance. The formula for the well and its mirror well is

.. math:: s_{r,t}=\frac{Q}{4\pi kD}\left(\mathrm{W}\left(\frac{r_{1}^{2}S}{4kDt}\right)-\mathrm{W}\left(\frac{r_{2}^{2}S}{4kDt}\right)\right)

In which :math:`r_{1}=50` m and :math:`r_{2}=450` m, :math:`\text{kD}\ =\ 1200` m2/d, :math:`S=0.2`

We also have :math:`\frac{Q}{4\pi\text{kD}}=\frac{1200}{4\pi1200}=0.08`

Then for t=7 days

:math:`u_{1}=1.49\times10^{-2}`, :math:`u_{2}=1.21`,

:math:`1\text{/}u_{1}=6.72\times10^{+1}`, :math:`1\text{/}u_{2}=8.30\times10^{-1}`, Then read the values for :math:`W(1/u)` from the Theis type graph, which yields the following numbers (however yours may be a bit different because it’s difficult to read exact numbers from a graph.

:math:`W\left(1.49\times10^{-2}\right)=3.6`, :math:`W(1.21)=0.16`

So the drawdown after 7 days in point p is

:math:`s_{t=7}=0.08\times(3.5-0.16)=0.28` m

--------------

#. What will be the drawdown at point p 14 days after the start of the extraction, i.e. 7 days after the well has started pumping?

--------------

For t = 14 days continuous pumping the values become

:math:`u_{1}=7.44\times10^{-3}`, :math:`u_{2}=6.03\times10^{-1}`,

:math:`1\text{/}u_{1}=1.43\times10^{+2}`, :math:`1\text{/}u_{2}=1.66`, read the values of :math:`\mathrm{W}(1/u)` from the Theis type curve to get the following values (which again may be a bit different from yours due to the accuracy with which you can read the numbers from a graph):

:math:`\mathrm{W}\left(7.44\times10^{-3}\right)=4.3`, :math:`\mathrm{W}\left(6.03\times10^{-1}\right)=0.45`

Hence the drawdown for :math:`t=14\,\mathrm{d}` of continued pumping would be

:math:`s_{t=14}=0.08\times(4.30-0.45)=0.31\,\mathrm{m}`.

The actual drawdown after 14 days will be that of continuous pumpoing (0.31 m) minus that of 7 days continuous pumping (0.28 m) because the pump was switched off after 7 days. We, therefore, after 14 days we only have a remaining drawdown equal to 0.31 – 0.28 = 0.03 m.

--------------

Question 2
----------

The picture shows an aquifer bounded by a fully penetrating river at *x=0*. The aquifer is unbounded to the right and has a transmissivity and a specific yield as indicated in the picture. Note that the transmissivity may be considered constant. The river water level varies continuously according to a sine-wave with a cycle time of *T= 1* d and an amplitude of *A=1.2* m.

.. container:: centering

   .. figure:: pictures/2022_3.png
      :alt: Aquifer bounded by fully penetrating water body with fluctuating water level at x=0. The aquifer extents at the right to infinity. Shown is the water table (or head) at an arbitrary time.
      :width: 80.0%

      Aquifer bounded by fully penetrating water body with fluctuating water level at x=0. The aquifer extents at the right to infinity. Shown is the water table (or head) at an arbitrary time.

#. What is the maximum and minimum head at *x = 25* m and at *x = 100* m?

#. What will be the drawdown at point p 14 days after the start of the extraction, i.e., 7 days after the well has started pumping?

#. By how much (i.e., by how large a factor) does this delay change if the storage coefficient would be 100 times as small as the given value, i.e., if it would be :math:`S=0.001` instead of :math:`S=0.1`?

--------------

The formula for the head in this aquifer is

.. math:: s(x,t)=Ae^{-\text{ax}}\sin\left(\omega t-ax\right)

With :math:`a=\sqrt{\frac{\omega S}{2\text{kD}}}`, the damping factor and :math:`\omega T=2\pi\rightarrow\omega=\frac{2\pi}{T}`

The maximum and minimum head at any x is given by :math:`s_{\max,\min}=\pm Ae^{-\text{ax}}`, the so-called envelope.

:math:`\omega=\frac{2\pi}{T}=\frac{2\pi}{1}=6.28` radians/day

:math:`a=\sqrt{\frac{\omega S}{2\text{kD}}}=\sqrt{\frac{6.28\times0.1}{2\times600}}=0.023` [1/m]

At :math:`x=25\,\mathrm{m}`, we have :math:`s_{\min,\max}=\pm Ae^{-\text{ax}}=\pm1.2e^{-0.023\times25}=\pm0.68\,\mathrm{m}`.

At :math:`x=100\,\mathrm{m}`, we have :math:`s_{\min,\max}=\pm Ae^{-\text{ax}}=\pm1.2e^{-0.023\times100}=\pm0.12\,\mathrm{m}`.

What is the delay of the wave at *x = 100* m relative to the wave at *x = 0* m?

The velocity of the wave follows from the argument of the sin being constant

.. math:: \omega t-ax=\mathrm{const}

Taking the derivative with respect to *t* yields

.. math:: \omega-a\frac{dx}{dt}=0

And so

   :math:`v=\frac{dx}{dt}=\frac{\omega}{a}=\frac{6.28}{0.023}\approx270\,\mathrm{m/d}`.

Hence, the delay at :math:`x=100\,\mathrm{m}` is :math:`100\text{/}270=0.37\,\mathrm{d}\approx9\,\mathrm{h}`.

--------------

Question 3:
-----------

The picture below shows an aquifer of limited lateral extent. To the left, at *x = 0*, it is bounded by a fully penetrating surface water body, such as a lake. To the right, at *x = L*, it is bounded by an impervious land mass as shown. The aquifer properties are shown in the picture, but you don’t need them to answer the questions. The water level of the lake and the groundwater table are initially flat at a level equal to *h=0* m as indicated by the horizontal blue line. At :math:`t\ =\ 0`, the water level of the lake suddenly changes upward by an amount *A* as indicated. Ignore other hydrological features like rain and evapotranspiration. Only the effect of the sudden change of the lake level is considered.

.. container:: centering

   .. figure:: pictures/2022_4.png
      :alt: Picture of the aquifer with fully penetrating water body at :math:`x=0` and impervious mass at :math:`x=L`
      :width: 80.0%

      Picture of the aquifer with fully penetrating water body at :math:`x=0` and impervious mass at :math:`x=L`

#. What are the boundary conditions at *x=0* and *x=L*?

--------------

The boundary condtions are a) fixed head at :math:`x=0` and b) zero flow at :math:`x=L`.

--------------

#. Describe how the head in the aquifer will develop over time due to the sudden change at *x=0* and *t=0*. Your description must include the situation at :math:`t=0` and at :math:`t=\infty`.

--------------

At :math:`t<0`, :math:`s=0` everywhere. At :math:`t=0^{+}`, :math:`s=A` at :math:`x=0` and :math:`s=0` everywhere else. At :math:`t>0`, :math:`s=A` at :math:`x=0` and :math:`A>s>0` everywhere else with :math:`s_{x>x_{1}}<s_{x<x_{1}}`\ for arbitrary :math:`x` and, finally, :math:`s=A` everywhere for :math:`t=\infty`.

--------------

Closed-book exam (1h), Feb 23, 2021
===================================

.. _question-1-1:

Question 1
----------

#. When pumping from a confined aquifer, all extracted water comes from storage. But what is the precise physical mechanism that causes the release of water from this type of aquifer? Explain.

--------------

Compression of the aquifer matrix and expansion of the water (combined elastic response of the aquifer with its water)

--------------

#. What is the so-called air-entry pressure and how does it relate to the capillary fringe? Explain.

--------------

This is the air pressure required to blow air through a sample of initially saturated soil. It’s a measure of the widest pores and coincides with the thickness of the capillary zone.

--------------

#. A confined aquifer system has a loading efficiency of LE = 0.6. If the barometer pressure increases with the equivalent of 40 cm water column, by how much does the pressure in the aquifer change? By how much does the head (water level in a piezometer in this aquifer) change? Explain and show.

--------------

A loading efficiency of 60% implies that 60 % of the load at ground surface will be supported by the water. Hence a loading at ground surface by the barometer, which also exercises 100% at the water level in the piezometer will cause a decline of the head in the piezometer by 40% of the load, which, in this case is 40% of 40 cm = 16 cm.

--------------

#. What is the difference between a Theis and a Hantush situation? The answer must contain the difference between the two situations as and what the physical origin is of the water pumped from a well in both these situations.

--------------

In the Theis situation all extracted water is released from storage and from storage only, while in the Hantush situation it also originates from the leakage through a top or bottom aquitard induced by the drawdown. The Theis drawdown, whether due to pumping a confined or an unconfined aquifer will never reach equilibrium. However a Hantush drawdown will reach equilibrium because the induced flow through the aquitard is proportional to the local induced head difference and therefore will eventually balance the extraction.

--------------

.. _question-2-1:

Question 2
----------

The solution for the head in a confined aquifer driven by surface water that varies according to a sine at x=0 is given by

.. math:: h_{x,t}=Ae^{-ax}\sin\left(\omega t-ax\right)\text{, with }a=\sqrt{\frac{\omega}{2}\frac{S}{kD}}

#. Explain what the parameters are with their dimension

--------------

:math:`h` is dynamic head [m], :math:`A` amplitude of river stage [m], :math:`a` [1/m] damping factor, :math:`\omega` [rad/time] is angular velocity of sine wave. :math:`T` [d] time, :math:`x` [m] distance from the river, :math:`S` [-] storage coefficient either elastic or specific yield, :math:`kD\ \mathrm{m^{2}/d}` transmissivity of the aquifer.

--------------

#. What is the velocity of the wave in the subsurface? Explain mathematically.

--------------

Take the argument of the sine as a constant hence :math:`\omega t-ax=const` and take the derivative with respect to time to get the velocity :math:`\frac{dx}{dt}=v=\frac{\omega}{a}`

--------------

#. What are the so-called envelopes? Explain and show them mathematically.

--------------

The two envelopes show the maximum amplitude as a function of x, hence :math:`H_{x}=\pm e^{-ax}`

The dynamic change of head in a strip of land of limited width like the one that is shown below can be computed using the simple formula for a half-infinite aquifer, but then we must apply superposition using so-called mirror ditches. In the figure below the water level at the left-hand side has just jumped up by *A* m and that at the right-and side by *B* m. The head for :math:`t=0.29\,\mathrm{d}` is shown. The lower picture shows the applied mirror/superposition scheme.

--------------

.. _question-3-1:

Question 3:
-----------

The dynamic change of head in a strip of land of limited width like the one that is shown below can be computed using the simple formula for a half-infinite aquifer, but then we must apply superposition using so-called mirror ditches. In the figure below the water level at the left-hand side has just jumped up by *A* m and that at the right-and side by *B* m. The head for t=0.29 d is shown. The lower picture shows the applied mirror/superposition scheme.

#. Is the shown mirror/superposition scheme used for the superposition correct? Clearly motivate your answer, a simple yes or no is not accepted.

--------------

The left and the right -hand boundaries are fixed. All errors to the left and the right of the left-hand boundary cancel, so only the fixed change at the left-hand boundary remains. This is ok. The same is true for the right-hand boundary. Hence, the superposition schme is correct.

--------------

.. container:: centering

   .. figure:: pictures/2021_1.png
      :alt: Strip of land bounded by fully penetrating surface water (top) and superposition scheme (bottom).
      :width: 80.0%

      Strip of land bounded by fully penetrating surface water (top) and superposition scheme (bottom).

Question 4:
-----------

During a pumping test with an extraction of :math:`Q=650\,\mathrm{m^{3}/d}`, the drawdown is measured in an observation well at :math:`r=50\,\mathrm{m}` distance from the well, sufficient to ignore any influence of partial penetration on the measurements. The measured drawdown in this piezometer is shown graphically versus the log of time in days.

.. container:: centering

   .. figure:: pictures/2021_2.png
      :alt: Measured drawdown during pumping test.
      :width: 80.0%

      Measured drawdown during pumping test.

The formula for the drawdown that is expected to fit the data for sufficiently large times is

.. math:: s_{r,t}\,=\,\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)

#. Do these data represent a Theis (confined/unconfined) or a Hantush (semi-confined) situation? Motivate your answer (a single yes or no is not accepted).

--------------

The curve represents a Theis drawdown, because there is no equilibrium.

--------------

#. Determine the transmissivity of the aquifer

--------------

We have:

.. math:: s_{r,t}=\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)=\frac{2.3\ Q}{4\pi kD}\log\left(\frac{2.25kDt}{r^{2}S}\right)

With

:math:`\Delta s_{r}=s_{r,10t}-s_{r,t}=\ \frac{2.3\ Q}{4\pi kD}\log\left(\frac{2.25kD10t}{r^{2}S}\right)-\frac{2.3\ Q}{4\pi kD}\log\left(\frac{2.25kD10t}{r^{2}S}\right)=\frac{2.3Q}{4\pi kD}\ \approx0.09\,\mathrm{m}`

It follows that

.. math:: 0.09\approx\frac{2.3Q}{4\pi kD}\rightarrow kD\approx\frac{2.3Q}{4\pi0.09}=\frac{2.3\times650}{4\pi0.09}\approx1300\,\mathrm{m^{2}\text{/}d}

--------------

#. Determine the storage coefficient of the aquifer

--------------

The storage coefficient can be computed from the zero drawdown in the logarithmic approximation of the Theis drawdown, i.e., when the argument of the log in the formula is one. This zero drawdown is at about :math:`t=0.1\,\mathrm{d}`, so :math:`S=\frac{2.25kDt}{r^{2}}=\frac{2.25\times1300\times0.1}{2500}\approx0.1`

--------------

#. What will be the radius of influence of this pumping test for *t* = 5 days?

--------------

The radius of influence is :math:`r=\sqrt{\frac{2.25kDt}{S}}=\sqrt{\frac{2.25\times1300\times5}{0.1}}\approx380` :math:`m`

--------------

Closed book exam (1h), Feb 4, 2020
==================================

.. _question-1-2:

Question 1
----------

#. Explain what is meant by air-entry pressure, and how you interpret it in terms of groundwater.

--------------

The air entry pressure is the pressure required to blow air through a small soil sample. It corresponds to the suction head of the widest pores, and, therefore, the thickness of the capillary fringe.

--------------

#. What happens to the water level in a piezometer installed in a confined aquifer if suddenly a load equivalent to a pressure increase :math:`\Delta p` is placed on ground surface?

--------------

The water pressure increases by *:math:`LE`* times :math:`\Delta p`. And the head in the piezometer goes up by :math:`\Delta\phi=LE\frac{\Delta p}{\rho g}`.

--------------

#. What happens to the water level in a piezometer if the barometer pressure suddenly change by an amount :math:`\Delta p`?

--------------

The water level would go up like answered in the previous question, but because of the full barometer pressure pushing down on the water level in the piezometer, it actually goes down by :math:`\Delta\phi=BE\frac{\Delta p}{\rho g}=\left(1-LE\right)\frac{\Delta p}{\rho f}`.

--------------

#. Explain what causes the difference between the answers to questions 2. And 3.

--------------

It’s already explained above.

--------------

#. If a pressure transducer is fixed in a piezometer, below the water level at a given elevation, then what changes would it register in the two situations described in questions 2 and 3? (A pressure transducer measures and registers the absolute pressure, i.e. water + air).

--------------

A pressure transducer measuring absolute pressure will experience a pressure increases of :math:`\Delta p` in both cases.

--------------

.. _question-2-2:

Question 2
----------

Let the time-dependent change of head in a strip of land with width *:math:`L`* [m] between two ditches be caused by a sudden change of water level equal to *:math:`A`* [m] at the left ditch and equal to *:math:`B`* [m] at the right ditch. We know that this can be computed using the formula that is valid for a half-infinite aquifer (that is an aquifer for which *:math:`x\ge0`*) bounded by surface water at :math:`x=0`, if we apply superposition. The formula for the half-infinite aquifer is

.. math:: s\left(x,t\right)=A\mathrm{erfc}\left(x\sqrt{\frac{S}{4kDt}}\right)

In preparation of the superposition, a superposition scheme is drawn (see figure below), showing the strip of land in dark yellow and the first few of the infinite series of mirror ditches. The arrows indicate the direction and size of the change of head at all ditches.

.. container:: centering

   .. figure:: pictures/2021_1.png
      :alt: Strip of land bounded by fully penetrating surface water (top) and superposition scheme (bottom).
      :width: 80.0%

      Strip of land bounded by fully penetrating surface water (top) and superposition scheme (bottom).

#. Is this scheme correct? Explain why or why not that is the case.

--------------

The scheme is correct because around the left ditch all mirror ditches cancel out except so that at the left ditch, only het head change at the left ditch remains. The same is true for the right ditch.

The first term of formula for drainage of a strip of land in which the head is at :math:`t=0` is uniform and equal to :math:`A` m above the ditches on either side is given by

.. math:: s\left(x,t\right)=A\frac{4}{\pi}\cos\left(\frac{\pi x}{2b}\right)\exp\left(-\left(\frac{\pi}{2}\right)^{2}\frac{t}{T}\right)\mbox{, with }T=\frac{b^{2}S}{kD}

--------------

#. What does this equation tell you? What’s happening here? What name would you give to *T* ? Also explain why.

--------------

The head between the diches has the shape of a cosine between :math:`-\pi/2` and :math:`+\pi/2` that declines exponentially with time. *:math:`T`* can be named characteristic time because its scales the actual time.

--------------

#. What is the halftime of this drainage process? Explain, and show it mathematically.

--------------

A halftime of a process is the time in which some outcome of the process is halved. Halftimes are a characteristic of exponential decay.

Mathematically just say that :math:`s_{t+\Delta t}=0.5s_{t}`, so

.. math:: \exp\left(-\left(\frac{\pi}{2}\right)^{2}\frac{t+\Delta t}{T}\right)=0.5\exp\left(-\left(\frac{\pi}{2}\right)^{2}\frac{t}{T}\right)

.. math:: -\left(\frac{\pi}{2}\right)^{2}\frac{t+\Delta t}{T}=\ln2+0.5\left(\frac{\pi}{2}\right)^{2}\frac{t}{T}

.. math:: \frac{\Delta t}{T}=\left(\frac{2}{\pi}\right)^{2}\ln2\approx0.28

--------------

#. How would you compare the rate of drainage of a desert that is 500 km wide between surface -water boundaries and an arable field of 100 m wide between ditches, if both have the same aquifer properties?

--------------

The characteristic time is :math:`T=\frac{b^{2}S}{kD}`, therefore,

.. math:: \frac{T_{\mathrm{desert}}}{T_{\mathrm{field}}}=\frac{b_{\mathrm{desert}}^{2}}{b_{\mathrm{field}}^{2}}=\frac{5^{2}\times10^{10}}{100^{2}}=25\times10^{6}

--------------

.. _question-3-2:

Question 3
----------

The simplified Theis solution for the drawdown due to a pumping well in a (un)confined aquifer reads

.. math:: s\left(r,t\right)=\frac{2.3Q}{4\pi kD}\log\left(\frac{2.25kDt}{r^{2}S}\right)

A pumping test was carried out with an extraction of :math:`Q=2400\,\mathrm{m^{3}/d}`. The drawdown was measured in 3 observation wells.

The figure shows the measured drawdown :math:`s` in the observation wells as a function of :math:`t/r^{2}` on logarithmic scale.

Answer the following questions

#. What is the transmissivity, explain and compute it.

--------------

The drawdown per log-cycle is about 0.55 m, which should equal

.. math:: s_{10t}-s_{t}=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kD10t}{r^{2}S}\right)-\log\left(\frac{2.25kDt}{r^{2}S}\right)\right]

.. math:: s_{10t}-s_{t}=\frac{2.3Q}{4\pi kD}\log\left(10\right)=\frac{2.3Q}{4\pi kD}=\frac{2.3\times2400}{4\pi kD}

Therefore,

.. math:: kD\approx800\,\mathrm{m^{2}/d}

--------------

#. What is the storage coefficient, explain and compute it?

--------------

Extending the straight portion of the drawdown curve to :math:`s=0` gives :math:`t/r^{2}=10^{-4}`. At this value, the argument of the logarithm must be 1, because then the computed drawdown is zero.

.. math:: \frac{2.25kDt}{r^{2}S}=1=\frac{2.24kD}{S}\times10^{-4}

.. math:: S=2.25\times800\times10^{-4}=0.018

--------------

#. If you had only the drawdown in the well itself instead of in observation wells? What could you and what could you not determine, and why?

--------------

In that case we can always compute the transmissivity, but not the storage coefficient, because the drawdown in the well depends on other things like borehole skin and partial penetration of the screen, which are not known in general.

--------------

#. What is the radius of influence? Explain and show it mathematically.

--------------

That’s the radius at which the drawdown in the simplified Theis formula is zero, so that then the argument of the logarithm is zero. In fact, this is what we used above to computed the storage coefficient, hence

.. math:: \frac{2.25kDt}{r^{2}S}=1\mbox{, so that }r=\sqrt{\frac{2.25kDt}{S}}

--------------

Closed book reexam (1h), March 2018
===================================

.. _question-1-3:

Question 1:
-----------

#. Explain what barometer efficiency (BE) is and how it physically works.

#. Explain in words what the characteristic halftime of an aquifer system says about the behavior of the system?

#. Consider the parameters :math:`L` (system width), :math:`kD` (transmissivity) and :math:`S_{y}` (specific yield), for each of these three parameters, does in increase make the characteristic time larger or smaller?

#. What is capillary rise and what has capillary rise to do with air-entry pressure?

#. When we extract water from a well in an infinitely extended aquifer, from where does all this extracted water come? Explain your answer.

--------------

#. | Barometer efficiency is the head decline due to barometer pressure increase, both expressed in pressure of head
   | 

     .. math:: BE=-\rho g\frac{\Delta\phi}{\Delta p}

#. | Characteristic half time of a groundwater system is the time during which the head above the fixed boundary is halved due to natural drainage alone. The characteristic time can be expressed as
   | 

     .. math:: T=\frac{L^{2}S}{4kD}=\frac{b^{2}S}{kD}

#. The L increases the halftime, like the S and the kD decreases the halftime as follows from the formula.

#. Capillary rise is the suction of water from the saturated zone into the unsaturated pore space. The air-entry pressure corresponds to the larger pores and hence to the thickness of the capillary zone.

#. All the extracted water comes from storage.

#. This is due to the volume in the system relative to the drainage rate.

--------------

.. _question-2-3:

Question 2:
-----------

Consider an aquifer in direct contact with the ocean. The tide of the ocean has an amplitude of :math:`A=1.0\:\mathrm{m}` and the cycle time is :math:`T=0.5\,\mathrm{d}` (one full tide in 12h). The aquifer is confined. The aquifer has the following properties: transmissivity :math:`kD=900\,\mathrm{m^{2}/d}` and storage coefficient :math:`S_{y}=0.002`. We are only interested in the effect of the tide land-inwards. The effect of the tidal fluctuation on the groundwater head land-inward, :math:`s`, obeys the following expression:

.. math:: s=A\,e^{-ax}\cos\left(\omega t-ax\right)\mbox{, where }a=\sqrt{\frac{\omega S}{2kD}}\mbox{, with }\omega=\frac{2\pi}{T}

Notice that the difference between the uppercase *S* and lowercase *s*.

#. Explain the parameters in the expression and given their dimension

--------------

:math:`s`:
   drawdown [L]

:math:`A`:
   amplitude [L]

:math:`x`:
   distance to where amplitude is given [L]

:math:`a`:
   damping [L\ :sup:`-1`\ ]

:math:`\omega`:
   angular velocity [radians/T] = [T\ :sup:`-1`\ ]

:math:`T`:
   cycle time [T]

--------------

#. What is the amplitude of the groundwater head fluctuation at 750 m from the ocean? Explain your answer in a few words and fist show it mathematically.

--------------

The amplitude only considers the damping, not the cosine,

.. math:: s=A\,e^{-ax}

Just fil in the values.

--------------

#. What is the delay of the head wave at 750 m from to the ocean with respect to the tide? Hint: compute the velocity of the tidal wave in the aquifer and then the time until the peak of the wave starting at the ocean reaches :math:`x=750\,\mathrm{m}`. Explain in a few words your approach and start with showing your answer mathematically.

--------------

Delay requires knowledge of the wave velocity. The velocity is obtained by realizing that the argument of the cosine must be constant when following the wave at its own speed

.. math:: \omega t-ax=\mathrm{const}

Take the derivative with respect to time

.. math:: \omega-a\frac{dx}{dt}=0

or

.. math:: \frac{dx}{dt}=\frac{\omega}{a}

The delay then is

.. math:: \Delta t=\frac{a}{\omega}\Delta x

The delay at :math:`x=L` is obtained by setting :math:`\Delta x=L`.

For the point at :math:`L=750\,m`, we have

.. math:: \Delta t_{1}=\frac{a_{1}}{\omega}L_{1}

Just fill in the numbers.

--------------

.. _question-3-3:

Question 3
----------

Consider a well in an infinite water-table (phreatic) aquifer. Drawdowns are small compared to the thickness of the aquifer, so that :math:`kD=900\,\mathrm{m^{2}/d}` may be considered constant. The specific yield, :math:`S_{y}=0.15`, is also constant. As there are no boundary conditions, the drawdown by the well follows the Theis equation. An approximation of which is

.. math:: s=\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)

#. Derive a mathematical expression for the so-called *radius of influence*, that is, the distance beyond which the drawdown can be neglected at a given time :math:`t`. Notice that :math:`\ln\left(\cdots\right)=2.3\log\left(\cdots\right)`.

--------------

The mathematical expression for the radius of influence is obtained by computing the radius for which the drawdown computed by this simplified formula is zero. That is for which the argument of the logarithm is 1.

.. math:: \frac{2.25kDt}{r^{2}S}=1

so that

.. math:: r=\sqrt{\frac{2.25kDt}{S}}

--------------

#. As you can see from the equation, the drawdown is (approximately) a logarithmic function in time. Derive a mathematical expression of the increase of the drawdown per log cycle of time, that is, between time *t* and time 10\ *t.*.

--------------

Simply subtract the drawdown at time :math:`10t` from that at time :math:`t`

.. math:: s_{10t}-s_{t}=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kD10t}{r^{2}S}\right)-\log\left(\frac{2.25kDt}{r^{2}S}\right)\right]=\frac{2.3Q}{4\pi kD}

--------------

#. The figure below shows an example of an actual drawdown measured at a piezometer at *r* = 100 m from the well extracting :math:`Q=1200\,\mathrm{m^{3}/d}`. Determine the transmissivity of the aquifer.

.. container:: centering

   .. figure:: pictures/2018_2.png
      :alt: Measured drawdown in piezometer at *:math:`r=100\,\mathrm{m}`* from well extracting :math:`Q=1200\,\mathrm{m^{3}/d}`
      :width: 80.0%

      Measured drawdown in piezometer at *:math:`r=100\,\mathrm{m}`* from well extracting :math:`Q=1200\,\mathrm{m^{3}/d}`

--------------

The drawdown per log cycle is 0.34 m. Hence,

.. math:: s_{10t}-s_{t}=0.34=\frac{2.3Q}{4\pi kD}

and so,

.. math:: kD=\frac{2.3Q}{4\pi\left(s_{10t}-s_{t}\right)}=\frac{2.3\times1200}{4\pi0.34}\approx645\,\mathrm{m^{2}/d}

--------------

#. Bonus question (extra points): Determine the storage coefficient.

--------------

The storage coefficient is obtained from the intersection of the tangent to the straight part of the graph with s=0, hence for which the argument of the log is 1.

.. math:: \frac{2.25kDt}{r^{2}S}=1

Therefore, with intersection time at :math:`t_{0}\approx1.0\,\mathrm{d}`

.. math:: S=\frac{2.25kDt_{0}}{r^{2}}=\frac{2.25\times625\times1.0}{100^{2}}=0.14

--------------

Closed book exam (1h), Feb 7, 2017
==================================

.. _question-1-4:

Question 1:
-----------

#. Someone says the barometer efficiency of the piezometer in his garden is 25%. What does that mean? Explain your answer telling how this phenomenon physically works.

--------------

A barometer efficiency of 25% implies a loading efficiency of 75%, i.e., that 75% of the load increment on ground surface is carried by the water and the remaining 25% by the soil skeleton. The increase of the pressure by 75% due to a load means a water table rise of 75% in the piezometer, however because it is the barometer that causes the load increase, the full 100% of the barometer pressure increase works on the water surface in the piezometer, so that the net effect for the water level is 75% up + 100% down = 25% down in the piezometer.

--------------

#. A pressure logger that is installed in this piezometer measures absolute pressure. What is absolute pressure? And what does this pressure gauge see when the barometer rises by the equivalent of 40 cm of water column, given the barometric efficiency of 25%?

--------------

The loading efficiency :math:`LE=1-BE=75%\ensuremath{\%}`. This is what is registered by the piezometer, :math:`0.75\times40\,\mathrm{cm}=30\,\mathrm{cm}` equivalent pressure rise.

--------------

#. What properties determine the value of the specific (elastic) storage coefficient?

--------------

The loading efficiency, i.e., the compressibility of the water and that of the skeleton of the aquifer matrix material.

--------------

#. What does the air-entry value have to do with the thickness of the capillary fringe/zone? Explain your answer.

--------------

The air-entry pressure corresponds to the thickness of the full capillary zone as it is the pressure required to blow air through the largest pores. So, this pressure corresponds to the capillary rise that matches the diameter of these largest pores.

The transient drawdown of a well with a constant extraction *Q* in the case without any head boundary condition is mathematically described by the Theis well drawdown:

.. math:: s=\frac{Q}{4\pi kD}\mathrm{W}\left(\frac{r^{2}S}{4kDt}\right)

that can be approximated by

.. math:: s\approx\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)

--------------

#. Sketch both graphs such that s is on a linear scale (downward positive) and time on a logarithmic horizontal scale. What’s the difference between the two?

--------------

A straight line (approximation) and a straight line that deviates asymptotically to zero for small drawdowns (Theis).

--------------

#. What is the drawdown per log-cycle of time, assuming that the approximation is valid?

--------------

Just ask what is :math:`s_{10t}-s_{t}`:

.. math:: s_{10t}-s_{t}=\frac{Q}{4\pi kD}\ln10=\frac{2.3Q}{4\pi kD}\log10=\frac{2.3Q}{4\pi kD}

--------------

#. What does ‘adius of influence‘ mean; how could you derive it from the above approximation?

--------------

The distance where :math:`s(r,t)=0`, i.e., set the argument of the log to one:

.. math:: s=0\rightarrow\frac{2.25kDt}{r^{2}S}=1\rightarrow r=\sqrt{\frac{2.25kDt}{S}}

--------------

#. Does the Theis drawdown reach a steady-state situation in the long run? Explain your answer.

--------------

The Theis drawdown has not steady state solution because all the pumped water comes from storage

--------------

We know the total discharge (flow) across a ring at fixed distance *r* from the well in a confined aquifer is given by

.. math:: Q_{r,t}=Q_{0}\,e^{-u}\mbox{, with }u=\frac{r^{2}S}{4kDt}

#. If you assume you are at a fixed distance r from the well, could you then formulate a characteristic time for the transient phenomenon :math:`Q(r,t)`? Explain your answer.

--------------

Just set

.. math:: u=\frac{r^{2}S}{4kDt}=\frac{T}{t}\rightarrow T=\frac{r^{2}S}{4kDt}

--------------

Below, we observe a hydrologist interpreting a transient pumping test in a confined aquifer. He/she plotted the drawdown data on a double log graph with drawdown *s* vertically upward and :math:`t/r^{2}` horizontally. The data of this graph with the measurements was then shifted over the Theis type-curve until the best possible match was obtained. This match is shown in the figure. Given that the extraction during the pumping test was :math:`Q=1200\,\mathrm{m^{3}/d}`.

#. Determine the transmissivity :math:`kD` and the storage coefficient :math:`S`.

.. container:: centering

   .. figure:: pictures/2017_1.png
      :alt: Measured drawdown curve matched with Theis type curve.
      :width: 100.0%

      Measured drawdown curve matched with Theis type curve.

--------------

Take two corresponding points on the vertical axis e.g.

.. math:: s=0.1\mbox{and }\mathrm{W}\left(u\right)=0.9

And on the horizontal axis:

.. math:: \frac{1}{u}=0.1\mbox{ and }\frac{t}{r^{2}}=4\times10^{-6}

Then

.. math:: \frac{s}{\mathrm{W\left(u\right)}}=\frac{Q}{4\pi kD}\rightarrow\frac{0.1}{0.9}=\frac{1200}{4\pi kD}\rightarrow kD=860\,\mathrm{m^{2}/d}

and

.. math:: \frac{1}{u}=\frac{4kD}{S}\frac{t}{r^{2}}\rightarrow S=4kD\frac{t/r^{2}}{1/u}=4kD\frac{4\times10^{-6}}{0.1}=4\times860\times4\times10^{-5}=0.14

--------------

.. _question-3-4:

Question 3:
-----------

Imagine the sea tide acting on a shore that has a confined aquifer inland with a constant *:math:`kD`* and *:math:`S`* in good vertical contact with the sea. The tide waves, which are characterized by *:math:`A`* and :math:`\omega`, therefore, penetrate the aquifer; they are mathematically described by:

.. math:: s_{x,t}=A\,e^{-ax}\sin\left(\omega t-ax\right)

#. As can be seen, this equation describes two simultaneous phenomena. Which are these two phenomena?

The factor *:math:`a`* in the equation was derived to be

.. math:: a=\sqrt{\frac{\omega S}{2kD}}

Damping of the wave with x and

#. What are the parameters with their dimensions?

--------------

:math:`s`:
   is the change of head relative to mean due to wave [m]

:math:`A`:
   is wave amplitude [m]

:math:`\omega`:
   is frequency, [rad/day] or [1/day]

:math:`S`:
   is storage coeffiicient [-]

:math:`kD`:
   is transmissivity [m\ :math:`^{2}`/d]

:math:`a`:
   damping [1/m]

--------------

#. A tidal wave has a frequency :math:`\omega` of two cycles per day of 24 hours, or a cycle time :math:`T` of 12 hours. Large wind waves, however, have a cycle time of only about 12 seconds. How far does the influence of these wind waves penetrate into the aquifer compared to the influence of the tide waves? Give their ratio and sketch the envelope of both to show this difference (the sketch does not have to be on scale).

--------------

The ratio of the damping due to different frequencies is, with index 1 referring to the low tidal frequency and index 2 to the fast wave frequency:

.. math:: \frac{a_{1}}{a_{2}}=\sqrt{\frac{\omega_{1}}{\omega_{2}}}=\sqrt{\frac{T_{2}}{T_{1}}}=\sqrt{\frac{12\,\mathrm{s}}{12\times3600\,\mathrm{s}}}=\sqrt{\frac{1}{3600}}=\frac{1}{60}

So that the damping of the fast wind wave is 60 times more that that of the slow tidal wave.

--------------

Closed book reexam (1h), Feb 2016
=================================

.. _question-1-5:

Question 1:
-----------

#. Explain what barometer efficiency (:math:`BE`) is and how it physically works.

#. Explain in words what the characteristic (half) time of a groundwater system is. What does is say about the behavior of the system?

#. For which of the parameters :math:`L` (system width), :math:`kD` (transmissivity) and :math:`S_{y}` (specific yield) would an increase make the characteristic system time smaller?

#. Explain why in hydrological logic you think that this is the case.

#. If you see a close-up of two grains held together by a small amount of water at their point of contact. What then is the pressure in that water? Explain why that is so.

--------------

#. | Barometer efficiency is the head decline due to barometer pressure increase, both expressed in pressure of head
   | 

     .. math:: BE=-\rho g\frac{\Delta\phi}{\Delta p_{a}}

#. | Characteristic half time of a groundwater system is the time during which the head above the fixed boundary is halved due to natural drainage alone. The characteristic time can be expressed as
   | 

     .. math:: T=\frac{L^{2}S}{kD}

#. Hence it is 4 times as long for a system with a double width; it is proportional to the storage coefficient and inversely proportional to the transmissivity of the groundwater system.

#. This is due to the volume in the system relative to the drainage rate.

#. The curvature of the free water surface between the grains shows that the pressure must be negative, which causes the cohesion between the grains.

--------------

.. _question-2-4:

Question 2:
-----------

Consider an aquifer in direct contact with the ocean. The tide of the ocean has an amplitude :math:`A=1.0\,\mathrm{m}` and the cycle time is :math:`T=0.5\,\mathrm{d}` (one full tide in 12h). The aquifer is confined. It consists of two parts. The first part reaches from the ocean to 500 m inland, the second part is present at more than 500 m from the ocean. The first part of the aquifer has the following properties: transmissivity :math:`kD=900\,\mathrm{m^{2}/d}` and storage coefficient :math:`S=0.002`. The second part of the aquifer has the following properties: :math:`kD=1800\,\mathrm{m^{2}/d}` and storage coefficient :math:`S=0.001`. Because we consider the fluctuation of the head to be superposed on the mean head, we are only interested in the head :math:`s` relative to the mean head at every location, that is, in :math:`s\left(x,t\right)=h\left(x,t\right)-h\left(x\right)`. This head fluctuation, :math:`s,` obeys following expression:

.. math:: s=A\,e^{-ax}\cos\left(\omega t-ax\right)\mbox{, where }a=\sqrt{\frac{\omega S}{2kD}}\mbox{ and }\omega=\frac{2\pi}{T}

Notice that the storage coefficient is capital :math:`S` and the head relative to the mean head is lowercase :math:`s`.

#. Explain the parameters in the expression and given their dimension

--------------

:math:`s`:
   drawdown [L]

:math:`A`:
   amplitude [L]

:math:`x`:
   distance to where amplitude is given [L]

:math:`a`:
   damping [L\ :sup:`-1`\ ]

:math:`\omega`:
   angular velocity [radians/T] = [T\ :sup:`-1`\ ]

:math:`T`:
   cycle time [T]

--------------

#. What is the amplitude of the groundwater head fluctuation, that is, the amplitude of :math:`s` in the aquifer at 500 m and at 1000 m from the ocean?

--------------

The amplitude only considers the damping, not the cosine,

.. math:: s=A\,e^{-ax}

For the first part use aquifer properties of that part, yielding :math:`s_{1}` and fill in :math:`x=L_{1}`

Hence,

.. math:: s_{1}=A\,e^{-aL_{1}}

The amplitude at :math:`x=L_{2}` can be computed relative to that at :math:`x=L_{1}`

.. math:: s_{2}=\left(A\,e^{-a_{1}L_{1}}\right)e^{-a_{2}\left(L_{2}-L_{1}\right)}

.. math:: s_{2}=A\,e^{-a_{1}L_{1}-a_{2}\left(L_{2}-L_{1}\right)}

--------------

#. What is the delay of the head wave at 500 m and 1000 m relative to the ocean tide? Hint: compute the velocity of the tidal wave in the aquifer and then the time until the peak of the wave starting at the ocean reaches :math:`x=500\,\mathrm{m}` and :math:`x=1000\,\mathrm{m}`.

--------------

Delay requires knowledge of the wave velocity. The velocity is obtained by realizing that the argument of the cosine must be constant when following the wave at its own speed

.. math:: \omega t-ax=\mathrm{const}

take the derivative with respect to time

.. math:: \omega-a\frac{dx}{dt}=0

or

.. math:: \frac{dx}{dt}=\frac{\omega}{a}

The delay then is

.. math:: \Delta t=\frac{a}{\omega}\Delta x

The delay at :math:`x=L_{1}` is obtained by setting :math:`\Delta x=L_{1}`

.. math:: \Delta t_{1}=\frac{a_{1}}{\omega}L_{1}

For the point at :math:`x=L_{2}` we have

.. math:: \Delta t_{2}=\frac{a_{2}}{\omega}\left(L_{2}\right)

Hence, the total delay up to the point :math:`x=L_{1}+L_{2}` would be

.. math:: \Delta t=\frac{a_{1}}{\omega}L_{1}+\frac{a_{2}}{\omega}L_{2}

--------------

.. _question-3-5:

Question 3:
-----------

Consider a well in an infinite water table (phreatic) aquifer. Drawdowns are considered small compared to the thickness of the aquifer, so that :math:`kD=900\,\mathrm{m^{2}d}` may be considered constant. The specific yield, :math:`S_{y}=0.15`, is also constant. As there are no boundary conditions, the drawdown by the well follows the Theis equation. An approximation of which is

.. math:: s\approx\frac{Q}{4\pi kD}\frac{2.3Q}{4\pi kD}\log\left(\frac{2.25kDt}{r^{2}S}\right)

#. Derive a mathematical expression for the so-called radius of influence, that is, the distance beyond which the drawdown can be neglected at a given time :math:`t` after the well was first switched on.

--------------

The mathematical expression for the radius of influence is obtained by computing the radius for which the drawdown computed by this simplified formula is zero. That is for which the argument of the logarithm is 1.

.. math:: \frac{2.25kDt}{r^{2}S}=1

so that

.. math:: r=\sqrt{\frac{2.25kDt}{S}}

--------------

#. As you can see, the drawdown is a logarithmic function in time. Derive a mathematical expression of the increase of the drawdown per log cycle, that is, between for instance :math:`t=6\,\mathrm{d}` and :math:`t=60\,\mathrm{d}`, or :math:`t=2\,\mathrm{d}` and :math:`t=20\,\mathrm{d}`.

--------------

Simply subtract the drawdown at :math:`t` from that at :math:`10t`

.. math:: s_{10t}-s_{t}=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kD\left(10t\right)}{r^{2}S}\right)-\log\left(\frac{2.25kDt}{r^{2}S}\right)\right]=\frac{2.3Q}{4\pi kD}

--------------

#. Assume the well has been continuously pumping for time :math:`t=t`, after which the extraction was stopped. What is the drawdown at distance :math:`r_{0}` at time is :math:`t=t_{1}+\Delta t` , where :math:`\Delta t` is any time passed since :math:`t_{1}`.

--------------

The drawdown at :math:`t+\Delta t` is obtained by superposition of an extraction *:math:`Q`* for the entire period from :math:`t` to :math:`t+\Delta t` and an extraction of :math:`-Q` for the period between :math:`t_{1}` and :math:`t_{1}+\Delta t`. Hence,

.. math:: s=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kD\left(t_{1}+\Delta t\right)}{r_{0}^{2}S}\right)-\log\left(\frac{2.25kD\Delta t}{r_{0}^{2}S}\right)\right]

.. math:: s=\frac{2.3Q}{4\pi kD}\log\left(\frac{t_{1}+\Delta t}{\Delta t}\right)

Under the condition that the logarithmic expression is valid for the considered point :math:`r_{0}` and times :math:`t\ge t_{1}`, otherwise we must apply the regular Theis equation, in which case we cannot simply combine two logarithms.

--------------

Closed-book exam (1h), Feb 1, 2016
==================================

Question 1: (16 points)
-----------------------

#. Explain loading efficiency, :math:`LE`.

--------------

:math:`LE` is the ratio of the pressure increase of the water in the (confined) aquifer and the pressure of the load on ground surface.

--------------

#. Explain the barometer efficiency, :math:`BE`.

--------------

The :math:`BE` is the ratio of the head decline measurable in a piezometer in the confined aquifer over the pressure increase of the barometer, both expressed in pressure units [N/m\ :math:`^{2}`\ ].

--------------

#. What is the difference registered by a pressure gauge in a confined aquifer measuring absolute pressure, given on the one hand a uniform mass placed at ground surface of weight :math:`\Delta p` N/m\ :sup:`2` and on the other hand a barometer increase of the same value of :math:`\Delta p\,\mathrm{N/m^{2}}`?

--------------

The absolute pressure in the confined aquifer increases by the same amount in both cases, i.e., :math:`LE\times\Delta p`. Of course, the head in the piezometer declines due to an increase of the barometer, but not the absolute pressure in the aquifer. (Only one student had this right).

--------------

#. What is the origin of delayed yield?

--------------

Delayed yield stems from delayed drawdown due to unconfined storage that manifests itself after the drawdown due to elastic, which is must faster due to the elastic storage coefficient that is about two orders of magnitude smaller than the phreatic storage or specific yield. Delayed yield may be encountered both in a phreatic aquifer and in semi-confined aquifers with an overlaying phreatic water table than cannot be maintained when it is affected by downward leakage into the pumped semi-confined aquifer below.

--------------

#. In which case does the influence of tide reach further inland into an aquifer?

The case with the higher or with the lower frequency?

--------------

The lower the frequency the further the reach, with zero frequency (that is, steady state), the reach is theoretically infinite. In reverse, with infinite frequency, the reach is zero, obviously.

--------------

The case with the larger or the smaller transmissivity *kD*?

--------------

The larger the *kD* the farther the inland reach of the tide. With infinite *kD*, the reach is infinite, with zero *kD* the reach is zero, obviously.

--------------

The case with the larger or with the smaller storage coefficient *S*?

--------------

The smaller the storage coefficient, the farther the tidal fluctuation reaches inland. With zero storage coefficient the reach is infinite, and with infinite storage coefficient, the reach is zero, obviously.

--------------

#. What is the difference between the situations with the wells that were studied by Theis and by Hantush?

--------------

Theis studies confined aquifers, including unconfined ones with constant transmissivity, in general, aquifers without external sources, in which all extracted water stems from storage alone.

Hantush studied semi-confined aquifers, aquifers in which the extracted water stems both from storage and from leakage from an overlying layer with constant head.

--------------

#. Does the Theis case have a final equilibrium drawdown? Explain your answer.

--------------

Because all water in the Theis case comes from storage there is no steady-stage drawdown possible.

--------------

#. Does the Hantush case have a final, steady-state drawdown? Explain your answer.

--------------

Because the part of the water from the overlaying layer is proportional to drawdown, there will be equilibrium in the end. So yes, there exists a st

--------------

Question 2: (14 points)
-----------------------

#. Explain what is the radius of influence of an extraction well in an aquifer of constant transmissivity and storage coefficient?

--------------

The radius of influence is the radius beyond which the (transient) drawdown is negligible.

--------------

#. | The simplified Theis solution is as follows:
   | 

     .. math:: s\left(r,t\right)\approx\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)

     From it derive an expression of the radius of influence.

--------------

| Set the argument of the log to 1 so that the log and with it the drawdown becomes zero. Then
| 

  .. math:: \frac{2.25kDt}{r^{2}S}=1\rightarrow r=\sqrt{\frac{2.25kDt}{S}}

--------------

#. Also show what is the drawdown difference per log cycle of time, that is, between time is :math:`t` and time is :math:`10t`.

--------------

The drawdown difference per log cycle (not ratio as some of you assumed) is

.. math:: s_{10t}-s_{t}=\frac{Q}{4\pi kD}\left[\ln\left(\frac{2.35kD\left(10t\right)}{r^{2}S}\right)-\ln\left(\frac{2.25kDt}{r^{2}S}\right)\right]=\frac{Q}{4\pi kD}\ln10=\frac{2.3Q}{4\pi kD}

--------------

#. Consider a well in a water table aquifer at 300 m from an impervious wall that reaches to the bottom of the aquifer. The aquifer has :math:`kD=600\,\mathrm{m^{2}d}` and the specific yield of :math:`S_{y}=0.2`. The pumping rate is :math:`Q=1200\,\mathrm{m^{3}/d}`. Assume that the approximation of the Theis equation that is given in this question is applicable. Compute the head change of the groundwater at the wall closest to the well.

--------------

Due to the presence of an impervious wall, we must use a mirror well that guarantees that there is no flow perpendicular to the wall. This mirror well must be placed on the other side of the wall at the same distance and its flow must be equal in both quantity and sign as that of the real well. The resulting drawdown is then the superposition of that of the well and its mirror well.

.. math:: s=\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r_{1}^{2}S}\right)+\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r_{2}^{2}S}\right)

.. math:: s=\frac{Q}{4\pi kD}\ln\left(\left[\frac{2.25kDt}{r_{1}r_{2}S}\right]^{2}\right)

.. math:: s=\frac{Q}{2\pi kD}\ln\left(\frac{2.25kDt}{r_{1}r_{2}S}\right)

with :math:`r=r_{1}=r_{2}=300\,\mathrm{m}`, so that

.. math:: s=\frac{Q}{2\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)

Just fill in the provided numbers to get the numerical answer.

--------------

Close-book exam (1h), Feb 2015
==============================

.. _question-1-6:

Question 1:
-----------

#. What types of storage or storage coefficients are associated with transient groundwater flow? And explain short how they physically work.

--------------

#. Elastic storage, from expansion and shrinking of the volume of the water ands the porous medium under changes of water and grain pressure.

#. Storage from decline of the water table, i.e., drainage of pores, drainage from the unsaturated zone.

--------------

#. Explain the relation between capillary rise and pore diameter.

--------------

Capillary rise is the net effect of attraction between water and grain surface (cohesion) and gravity. It may be expressed as upward attraction equals downward gravity force:

.. math:: 2\pi r\sigma\cos\gamma=\pi r^{2}\rho gh

Hence the capillary rise is inversely proportional to the effective pore radius *r*

.. math:: h=\frac{2\pi\sigma\cos\gamma}{\pi r^{2}\rho g}=\frac{1}{r}\frac{2\sigma\cos\gamma}{\rho g}

--------------

#. Explain the general shape of the moisture curve in the unsaturated zone. Describe where the water comes from when the water table is lowered.

--------------

The general shape of the moisture curve is straight at porosity upward from the water table to the top of the capillary zone and then declining upward as more and more pores fall dry depending on their pore size. At each elevation only the pore with radius smaller than elevations h above the water table will contain water, where h is computed with the previous formula. The actual shape varies with time as plants transpire from the root zone and downward or upward flow through the unsaturated zone also affect the exact shape of the moisture curve at any time.

--------------

#. Explain the difference between the loading efficiency (:math:`LE`) and the barometer efficiency (:math:`BE`)?

--------------

The loading efficiency is the increase in water pressure (or head) in a confined aquifer due to and relative to a load placed uniformly on ground surface. The barometric efficiency is same caused by an increase of the barometric pressure. However, due to the barometric pressure also working on the water surface in the piezometer, the head in the piezometer declines. The decline is such that :math:`LE+BE=1`.

--------------

#. When you see animal holes in the field, like rabbit, rat and worm holes, how much do you think these holes may contribute to the infiltration of rainwater during and after showers, to what extent are the animals living in those holes affected by heavy rains, and , finally, what would it take to swim them out of their holes? Explain your answer from your insight in how water in the subsurface behaves.

--------------

Animal holes stay dry if the zone they are in is unsaturated, which means that the pore pressure is negative, i.e., below the atmospheric pressure in the animal holes. Hence animals are not affected by rain, they are only affected when the water table rises above their bottom and the pore pressure becomes zero or positive. In that case the holes may collapse, as they become filled up with water and the animals are driven out of their homes.

--------------

.. _question-2-5:

Question 2:
-----------

Consider a confined aquifer in direct contact with the ocean in which the head fluctuates along with the tide of the ocean. The daily solar tide, with cycle time :math:`T=12\,\mathrm{h}` or, equivalently, :math:`T=0.5\,\mathrm{d}`, has amplitude :math:`A=2.5\,\mathrm{m}` and the 4 weekly moon tide, with cycle time :math:`T=1/28\,\mathrm{d}`, has amplitude or :math:`A=1\,\mathrm{m}`. The groundwater head in the aquifer relative to the mean value at time *:math:`t`* and distance *:math:`x`* from the ocean obeys to the following expression:

.. math:: s=Ae^{-ax}\cos\left(\omega t-ax\right)\mbox{, where }a=\sqrt{\frac{\omega S}{2kD}}

If *:math:`T`* is the time required for a complete cycle, then the angular velocity :math:`\omega=2\pi/T`.

Further, *:math:`kD=900\,\mathrm{m^{2}/d}`* and *:math:`S=0.001`*.

#. Explain the parameters in the expression and give their dimension.

--------------

:math:`x`:
   distance [L]

:math:`t`:
   time [T]

:math:`s`:
   drawdown [L] or difference from average

:math:`A`:
   amplitude of head wave [L]

:math:`\omega`:
   angle velocity [/T] or [radians/T]

:math:`S`:
   storage coefficient [-]

:math:`kD`:
   transmissivity [L\ :math:`^{2}`/T]

--------------

#. What is the amplitude of the groundwater fluctuation due to both tides individually at 500 and 2000 m from the coast? So, the twice-a-day tide amplitude at 500 m and at 2000 m and the 28-day tide amplitude at 500 m and 2000 m?

--------------

The wave amplitude is given by the envelope:

.. math:: s_{\mathrm{env},x}=\pm A\,e^{-ax}

The maximum amplitude for the daily tide at 500 and 2000 m and an amplitude A=2.5 m then becomes 0.67 and 0.013 m respectively and that due to the moon-tide with its much lower frequency at the same distances and an amplitude of A=1 m becomes 0.83 and 0.49 m respectively.

--------------

#. How much are the waves of both tides delayed at 500 m from the coast?

--------------

The delay time follows from the velocity of the wave obtained by setting :math:`\omega t=ax`, or :math:`\omega t-ax=\mathrm{const}` and then taking the derivative of the expression with respect to :math:`t`. From which follows :math:`v=\frac{x}{t}=\frac{dx}{dt}=\frac{\omega}{a}` or, equivalently for the delay :math:`t=\frac{x}{v}=\frac{a}{\omega}x`

--------------

#. Over what distance does the maximum tide-induced amplitude in the groundwater declines by a factor of two in both cases?

--------------

The distance over which the maximum amplitude declines by a factor 2 is readily obtained from

.. math:: A\,e^{-a\left(x+\Delta x\right)}=0.t\,A\,e^{-ax}

.. math:: a\left(x+\Delta x\right)=\ln2+ax

.. math:: \Delta x=\frac{\ln2}{a}

--------------

.. _question-3-6:

Question 3:
-----------

A groundwater table rise after it was agitated by a sudden recharge *N* [m] will decay over the thereafter. For a system of bounded by two parallel water courses at *L* mutual distance, this decline after some time can be approximated by the following expression:

.. math:: s=A\frac{4}{\pi}\cos\left(\pi\frac{x}{L}\right)\exp\left(-\left(\frac{\pi}{L}\right)^{2}\frac{kD}{S_{y}}t\right)

#. Describe the parameters and given their dimension.

--------------

See syllabus

--------------

#. Give an expression for the sudden rise A caused by a sudden recharge amount equal to N [m]:

--------------

.. math:: A=\frac{N}{S_{y}}

--------------

#. Describe in a few words what this expression is and does, so what does its graph look like and how does it behave over time.

--------------

The expression shows a cosine shaped water table spanned between the boundaries at :math:`x=\pm L/2` that declines exponentially over time.

--------------

#. Give an expression of what can be called characteristic time of this system.

--------------

We can write the argument of the exponent as :math:`t/T` with :math:`T` the characteristic time. Doing so, we have

.. math:: T=\left(\frac{L}{\pi}\right)^{2}\frac{S_{y}}{kD}

yielding

.. math:: s=A\frac{4}{\pi}\cos\left(\pi\frac{x}{L}\right)\exp\left(-\frac{t}{T}\right)

--------------

#. Derive an expression of the half time of this system.

--------------

If time proceeds by one halftime then the head declines by a factor of two

.. math:: \exp\left(-\frac{t+\Delta t_{\mathrm{50\%}}}{T}\right)=0.5\exp\left(-\frac{t}{T}\right)

.. math:: \Delta t_{\mathrm{50\%}}=\ln\left(2\right)T\approx0.69T

--------------

#. Derive an expression for the discharge of this system.

.. math:: Q_{x}=-kD\frac{\partial s}{\partial x}=kD\,A\frac{4}{L}\sin\left(\pi\frac{x}{L}\right)\exp\left(-\left(\frac{\pi}{2}\right)^{2}\frac{t}{T}\right)

The total discharge is obtained by multiplying by 2 the discharge at :math:`x=L/2`:

.. math:: Q_{x}=\frac{8A}{L}kD\sin\left(\frac{\pi}{2}\right)\exp\left(-\left(\frac{\pi}{2}\right)^{2}\frac{t}{T}\right)

.. _question-4-1:

Question 4:
-----------

A 300 m deep well in Jordan with borehole radius *:math:`r=0.25\,\mathrm{m}`* was drilled in a limestone aquifer to serve a refugee camp. The well was recently test pumped during one day at a rate of *:math:`Q=60\,\mathrm{m^{3}/h}`*. The head at 0, 0.01, 0.1 and 1 d after the start of the pump was 100, 135, 147 and 159 m below ground surface respectively. The pump is installed at 200 m below ground surface.

Further assume:

The estimated specific yield of this aquifer is 0.01.

The unknown transmissivity is constant.

You may use the simplified expression of transient drawdown in an infinite aquifer

.. math:: s\approx\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S}\right)

#. Estimate the transmissivity of this aquifer.

--------------

The transmissivity can be computed using the measured drawdowns, for instance

.. math:: s_{3}-s_{2}=\frac{Q}{4\pi kD}\left[\ln\left(\frac{2.25kDt_{3}}{r^{2}S}\right)=\ln\left(\frac{2.25kDt_{2}}{r^{2}S}\right)\right]

or

.. math:: s_{3}-s_{2}=\frac{Q}{4\pi kD}\ln\left(\frac{t_{3}}{t_{2}}\right)=\frac{Q}{4\pi kD}\ln\left(10\right)=2.3\frac{Q}{4\pi kD}

Hence,

.. math:: kD=\frac{2.3Q}{4\pi\left(s_{3}-s_{2}\right)}=\frac{2.3\times24\times60}{4\pi\left(159-147\right)}=22\,\mathrm{m^{2}/d}

--------------

#. How much will be the drawdown after 3 years (1000 d)? Is the pump at 200 m below ground surface (i.e., 100 m below the initial water table) still deep enough to pump the water up?

--------------

.. math:: s=\frac{Q}{4\pi kD}\ln\left(\frac{2.25kDt}{r^{2}S_{y}}\right)

.. math:: s_{2700}=\frac{24\times60}{4\pi22}\ln\left(\frac{2.25\times22\times1000}{0.25^{2}\times0.01}\right)=95\,\mathrm{m}

This means that the well can be pumped continuously at the given rate. But also, that other wells in the camp may prevent that because they lower the head at this well too.

--------------

#. Another well of equal size, depth and flow rate is planned at a second location in the camp at 2 km distance. How much will be the drawdown in each well after 3 years (1000 days) in this case? Assume that both wells pump for the same period. How deep should the pumps be installed to allow pumping both wells at he given rate for 3 years?

--------------

.. container:: list

   .. math:: s=\frac{Q}{4\pi kD}\left[\ln\left(\frac{2.25kDt}{r_{0}^{2}S_{y}}\right)+\ln\left(\frac{2.25kDt}{r_{1}^{2}S_{y}}\right)\right]

   .. math:: s=\frac{Q}{4\pi kD}\ln\left(\left[\frac{2.25kDt}{r_{0}r_{1}S_{y}}\right]^{2}\right)

   .. math:: s=\frac{Q}{2\pi kD}\ln\left(\frac{2.25kDt}{r_{0}r_{1}S_{y}}\right)

   .. math:: s=\frac{24\times60}{4\pi22}\ln\left(\frac{2.25\times22\times1000}{0.25\times2000\times0.01}\right)=96\,\mathrm{m}

This means that the pumps are still submersed after 1000 days. Notice that if we compute the drawdown using the Theis equation instead of the logarithmic simplification, the computed drawdown would be 2 m more. After about 1500 days the drawdown would cause the pump to fall dry. This can be seen if a graph of the drawdown versus time is made.

--------------

Closed-book reexam (1h), March 2015
===================================

.. _question-1-7:

Question 1:
-----------

#. Explain what barometer efficiency (:math:`BE`) is and how it physically works?

#. When you see animal holes in the field, like rabbit, rat and worm holes, how much do you think these holes may contribute to the infiltration of rainwater during and after showers, to what extent are the animals living in those holes affected by heavy rains, and , finally, what would it take to swim them out of their holes? Explain your answer from your insight in how water in the subsurface behaves.

Qustion 2:
----------

Consider an aquifer in direct contact with the ocean. The tide of the ocean has an amplitude :math:`A=1\,\mathrm{m}`\ m and cycle time is *T* = 0.5 d (one full tide in 12h).

The aquifer is confined. It consists of two parts. The first part reaches from the ocean to 500 m in land, the second part is present at more than 500 m from the ocean.

The first part of the aquifer has the following properties: transmissivity :math:`kD=900\,\mathrm{m^{2}/d}` and storage coefficient :math:`S=0.002`.

The second part of the aquifer has the following properties, :math:`kD=1800\,\mathrm{m^{2}/d}` m\ :sup:`2`/d and storage coefficient :math:`S=0.001`.

Because we consider the fluctuation of the head to be superposed on the mean head, we are only interested in the head, :math:`s`, relative to the mean head at every location, that is :math:`s\left(x,t\right)=h\left(x,t\right)-h\left(x\right)`. This head fluctuation, :math:`s`, obeys following expression:

.. math:: s=A\,e^{-ax}\cos\left(\omega t-ax\right)\mbox{, where }a=\sqrt{\frac{\omega S}{2kD}}\mbox{ and }\omega=\frac{2\pi}{T}

Notice that the storage coefficient is capital :math:`S` and the head relative to the mean head is lower case :math:`s`.

#. Explain the parameters in the expression and give their dimension.

#. What is the amplitude of the groundwater head fluctuation, that is, the amplitude of :math:`s`, in the aquifer at 500 m and at 1000 m from the ocean?

--------------

The amplitude at distance :math:`0\le x\le500\,\mathrm{m}` is

.. math:: A_{x\le L}=A_{0}\exp\left(-a_{1}x\right)

.. math:: A_{x\ge L}=A_{0}\exp\left(-a_{1}L\right)\exp\left(a_{2}\left(x-L\right)\right)\mbox{, where }x\ge L

--------------

#. What is the delay of the head wave at 500 and 1000 m relative to the ocean tide? Hint: compute the velocity of the tidal wave in the aquifer and then the time until the peak of the wave starting at the ocean reaches :math:`x=500\,\mathrm{m}` and :math:`x=1000\,\mathrm{m}`?

--------------

The velocity of the wave follows from :math:`\omega t-ax=\mathrm{const}`. We can take :math:`\mathrm{const}=0` and say :math:`v=\frac{x}{t}=\frac{\omega}{a}` , or more formally take the derivative of the expression with respect to :math:`t` to get:

.. math:: \omega-a\frac{dx}{dt}=0\rightarrow v=\frac{dx}{dt}=\frac{\omega}{a}=\sqrt{2\omega\frac{kD}{S_{y}}}

The time :math:`t_{1}` for the wave peak to reach :math:`x=L` then equals :math:`t_{1}=\frac{L}{v_{1}}`.

The time :math:`t_{2}` for the wave to reach any point :math:`x>L` then is

.. math:: t_{2}=\frac{L}{v_{1}}+\frac{x-L}{v_{2}}\mbox{, where }v_{1}=\frac{\omega}{a_{1}}\mbox{ and }v_{2}=\frac{\omega}{a_{2}}

--------------

.. _question-3-7:

Question 3:
-----------

Consider a well in an infinite water-table (phreatic) aquifer. Drawdowns are considered small compared to the thickness of the aquifer, so that :math:`kD=900\,\mathrm{m^{2}/d}` may be considered constant. The specific yield, :math:`S_{y}=0.15`, is also constant. As there are no boundary conditions, the drawdown by the well follows the Theis equation. An approximation of which is

.. math:: s\approx\frac{2.3Q}{4\pi kD}\log\left(\frac{2.25kDt}{r^{2}S}\right)

#. Derive a mathematical expression for the so-called radius of influence, that is, the distance beyond which the drawdown can be neglected at a given time :math:`t` after the well was first switched on.

--------------

We just have to set :math:`s=0`, that is, the argument of the logarithm is 1

.. math:: \frac{2.25kDt}{r^{2}S_{y}}=1\rightarrow r=\sqrt{\frac{2.25kDt}{S}}

--------------

#. As you can see the drawdown is logarithmic in time. Derive a mathematical expression for the increase of the drawdown per log cycle, that is between for instance *:math:`t=6\,\mathrm{d}`* and *:math:`t=60\,\mathrm{d}`* days, or *:math:`t=2\,\mathrm{d}`* days and *:math:`t=20\,\mathrm{d}`*.

--------------

In this case we compare the drawdown after :math:`t=10\Delta t` with :math:`t=\Delta t`:

.. math:: s_{10\Delta t}-s_{\Delta t}=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kD\left(10\Delta t\right)}{r^{2}S}\right)-\log\left(\frac{2.25kD\Delta t}{r^{2}S}\right)\right]=\frac{2.3Q}{4\pi kD}

--------------

#. Assume the well has been continuously pumping for time :math:`t=t_{1}`, after which the extraction was stopped. What is the drawdown at distance :math:`r_{0}` at time :math:`t=t_{1}+\Delta t` , where :math:`\Delta t` is any time passed since :math:`t_{1}`.

--------------

.. math:: s_{t_{1}+\Delta t}-s_{t_{1}}=\frac{2.3Q}{4\pi kD}\log\left(\frac{t_{1}+\Delta t}{t_{1}}\right)

--------------

Closed-book exam (1h), Feb 2014
===============================

.. _question-1-8:

Question 1:
-----------

#. What types of storage or storage coefficients are associated with transient groundwater flow?

--------------

-  Phreactic of water-table storage,due to filling and emptying of pores. The corresponding storage coefficient is called specific yield :math:`S_{y}\,\mathrm{[-]}`

-  Elastic storage which is due to compression and expansion of the water and the porous matrix. The corresponding storage coefficient is called :math:`S\,\mathrm{[-]}`

--------------

#. Explain how these types of storage physically work.

--------------

#. Storage due to drainage of pores.

#. Storage due to elasticity of water and the porous medium

--------------

#. Explain the relation between capillary fringe and air entry pressure.

--------------

The capillary fringe and the air-entry pressure are equivalent. It is the pressure required to flow air through the largest pores down to the water table. It is also the height over which water is sucked up into the largest pores from the water table.

--------------

#. Explain the difference between the loading efficiency (:math:`LE`) and the barometer efficiency (:math:`BE`)?

--------------

The loading efficiency is the increase in water pressure (or head) in a confined aquifer due to and relative to a load placed uniformly on ground surface. The barometric efficiency is same caused by an increase of the barometric pressure. However, due to the barometric pressure also working on the water surface in the piezometer, the head in the piezometer declines. The decline is such that :math:`LE+BE=1`.

--------------

#. Why does the specific yield of unconfined aquifers with a shallow groundwater table depend on the depth of the water table?

--------------

This is due to the moisture profile above the water table. When the water table is shallow, part of this profile is above ground surface and will no longer contribute to drainage and therefore, reduces the specific yield.

--------------

#. What is halftime when considering decay of a water mound between rivers? How would you describe it?

--------------

The halftime is the time in which de difference between the head or the elevation of the water table between the river is reduced by 50%. The halftime is determined by :math:`L`, :math:`kD` and :math:`S`.

--------------

#. Assume the well has been continuously pumping for time :math:`t=t_{1}`, after which the extraction was stopped. What is the drawdown at distance :math:`r_{0}` at time :math:`t=t_{1}+\Delta t` , where :math:`\Delta t` is any time passed since :math:`t_{1}`.

--------------

A formula for the characteristic time of a groundwater basin of width :math:`L` is *:math:`T=L^{2}S/\left(4kDt\right)`* with halftime :math:`T_{\mathrm{50\%}}=\ln\left(2\right)T`. The formula shows that *:math:`L`* and *:math:`S`* increase the halftime and *:math:`kD`* decreases the halftime.

--------------

.. _question-2-6:

Question 2:
-----------

Consider a confined aquifer in direct contact with the ocean in which the head fluctuates along with the tide of the ocean. The tide has an amplitude of :math:`a=2.5\,\mathrm{m}`. The groundwater head in the aquifer at time *t* and distance *x* from the ocean obeys to the following expression:

.. math:: s=a\,e^{-ax}\cos\left(\omega t-ax\right)\mbox{, where }a=\sqrt{\frac{\omega S}{2kD}}

The frequency :math:`f` of the tide is one complete cycle per 24 hours, i.e. :math:`f=1/d`, with, of course, :math:`\omega=2\pi f`.

We don’t know the value of *:math:`kD`* and :math:`S`, but we have measured the amplitude of the groundwater head fluctuation at . This amplitude is 25 cm, one tenth of that of the ocean.

#. Explain the parameters in the expression and give their dimension.

--------------

:math:`x`:
   distance [L]

:math:`t`:
   time [T]

:math:`s`:
   drawdown [L] or difference from average

:math:`A`:
   amplitude of head wave [L]

:math:`\omega`:
   angle velocity [/T] or [radians/T]

:math:`S`:
   storage coefficient [-]

:math:`kD`:
   transmissivity [L\ :math:`^{2}`/T]

--------------

#. Give an expression for the amplitude at distance x from the ocean.

--------------

The amplitude is independent of the cosine. Hence,

.. math:: \pm A_{x}=\pm A_{0}\,e^{-ax}

--------------

#. With the given information, compute parameter *a*, and the diffusivity of the aquifer, i.e. the ratio :math:`kD/S`.

--------------

The amplitude, :math:`s_{0}=2.5\,\mathrm{m}`, is given at distance :math:`x=0` at the sea and as :math:`s_{1}=0.1s_{0}` at :math:`x=x_{1}=500\,\mathrm{m}`, therefore,

.. math:: ax_{1}=\ln\left(\frac{s_{0}}{s_{1}}\right)\rightarrow a=\frac{\ln10}{500}\approx\frac{1}{220}

The diffusivity then follows from :math:`a^{2}=\frac{\omega S}{2kD}`, therefore, with :math:`T=1\,\mathrm{d}`,

.. math:: \frac{kD}{S}=\frac{\omega}{2a^{2}}=\frac{2\pi/1}{2}220^{2}=1.5\times10^{5}\,\mathrm{m^{2}/d}

--------------

#. Give an expression for the velocity of the wave of the groundwater-head in the subsurface? How much is this velocity?

--------------

The velocity of the wave of the head is found from the argument under the cosine, it must be constant, or zero for convenience

.. math:: \omega t-ax=0\rightarrow\frac{x}{t}=v=\frac{\omega}{a}=\frac{2\pi}{1}\times220\approx1380\,\mathrm{m/d}=58\,\mathrm{m/h}

--------------

Qestion 3:
----------

Consider an unconfined aquifer with conductivity :math:`k=10\,\mathrm{m/d}`, a specific yield of :math:`S_{y}=0.1` and an initial thickness . A well is located in this aquifer on each of the four corners of a square with sides of :math:`L=200\,\mathrm{m}`. The wells start pumping at :math:`t=0`. They pump with a rate of :math:`Q=120\,\mathrm{m^{3}/d}` for 1d, after which they stop.

The drawdown according to Theis is

.. math:: s=\frac{Q}{4\pi kD}\mathrm{W}\left(u\right)\mbox{, where }u=\frac{r^{2}S}{4kDt}

The Theis well function is graphically given in Figure 1 below.

#. Compute the drawdown in the center of the square after :math:`t=2\,\mathrm{d}`. You may neglect the change of the transmissivity caused by the change of the water depth in the aquifer.

.. _question-4-2:

Question 4
----------

Given that the well function can be computed by the following infinite series

.. math:: \mathrm{W}\left(u\right)=-\gamma-\ln u+u-\frac{u^{2}}{2\times2!}+\frac{u^{3}}{3\times3!}-\frac{u^{4}}{4\times4!}+\cdots

with :math:`\gamma=0.577216\cdots` and :math:`u=r^{2}S/\left(4kDt\right)`

#. What would be a good approximation of the drawdown for small values of :math:`u`? (Assume for instance that *u*\ <0.01). Notice for mathematical convenience, that :math:`\gamma=\ln\left(e^{\gamma}\right)`.

--------------

Truncate the series beyond and including :math:`u`, which is allowed for small values of :math:`u`. We are then left with the following approximation

.. math:: \mathrm{W}\left(u\right)\approx-\gamma-\ln u

The fill in :math:`u` and :math:`\gamma` to obtain

.. math:: \mathrm{W}\left(u\right)\approx\ln\left(\frac{2.25kDt}{r^{2}S}\right)

--------------

#. How could you define the radius of influence of the drawdown? Use the formula for the drawdown from the previous question together with the approximation from the previous question.

--------------

Set the drawdown in the approximation of the Theis well function equal to 0, i.e. :math:`\mathrm{W}\left(u\right)=0` to obtain

.. math:: \frac{2.25kDt}{r^{2}S}=1\rightarrow r=\sqrt{\frac{2.25kDt}{S}}

--------------

.. container:: centering

   .. figure:: pictures/2014_1.png
      :alt: Theis well function type curve, ie, :math:`\mathrm{W}\left(u\right)` versus :math:`1/u`.
      :width: 80.0%

      Theis well function type curve, ie, :math:`\mathrm{W}\left(u\right)` versus :math:`1/u`.

Closed-book exam (1h), Feb 3, 2011
==================================

Question 1: Pressure in confined aquifer
----------------------------------------

Question 1: Pressure in confined aquifer

A water level in a piezometer in a confined aquifer is affected if the weight on a ground surface is suddenly changed. Compare two situations a) Sudden change by a load placed on the ground, such as sand or flooding by water and b) Sudden increase of the barometric pressure.

Case a: — a load is placed on ground surface

#. How does the water pressure change in the piezometer? (Up? Down? Not?)

--------------

Up

--------------

#. How does the head change in the piezometer? (Up? Down? Not?)

--------------

Up

--------------

Case b: — barometer pressure increased

#. How does the water pressure change in the piezometer? (Up? Down? Not?

--------------

Up

--------------

#. How does the head change in the piezometer? (Up? Down? Not?)

--------------

Down

--------------

#. If there is a difference between the two cases, then why is that?

--------------

Although the water pressure in increased by the same amount in both cases, the water level in the piezometer goes down in the case of the increased barometric pressure, because the air pressure works for 100% on the water level inside the piezometer which is greater than the increase of water pressure in the aquifer due to the air pressure on ground surface. In the case of an increased load there is no increase of pressure on the water level in the piezometer, and so the change of water level in the piezometer fully reflects the change of water pressure in the aquifer, which is some fraction of the increase of pressure on ground surface.

--------------

Question 2: Tidal waves
-----------------------

The groundwater head variation in a confined aquifer due to a tidal wave at x=0 can be expressed mathematically as follows:

.. math:: s\left(x,t\right)=\phi\left(x,t\right)-\phi_{0}+A\,\exp\left(-ax\right)\sin\left(\omega t-ax\right)\mbox{, in which }a=\sqrt{\frac{\omega S}{2kD}}

and :math:`\omega=\frac{2\pi}{T}` with :math:`T` the period of the wave.

#. What is the amplitude of the wave at distance :math:`x`?

--------------

.. math:: A_{x}=A_{0}\,e^{-ax}

--------------

#. What is the velocity of the wave?

--------------

.. math:: \omega t-ax=\mathrm{const}=0\rightarrow v=\frac{x}{t}=\frac{\omega}{a}

--------------

#. If the wave would be just observable in a piezometer at x=1000 m from the coast, then at what distance would the wave be just observable on another spot along the coast where the storage coefficient is be 100 times greater than at the current spot and the transmissivity is the same?

--------------

So how to get the same amplitude at :math:`x=0` for both waves?

.. math:: A_{1}=A_{0}\,e^{-a_{1}L_{1}}=A_{0}\,e^{-a_{2}L_{2}}

so

.. math:: a_{1}L_{1}=a_{2}L_{2}

.. math:: \frac{\omega S_{1}}{2kD}L_{1}=\frac{\omega S_{2}}{2kD}L_{2}

.. math:: S_{1}L_{1}=S_{2}L_{2}

Therefore,

.. math:: L_{2}=L_{1}\frac{S_{1}}{S_{2}}=1000\times\frac{1}{100}=10\,\mathrm{m}

--------------

#. A tidal wave occurring daily is just observable in the aquifer at a distance of x=500 m from shore. At what distance from the shore will a 14-day wave be just observable occurring due to the monthly moon cycle? Assume the same amplitude for both waves.

--------------

.. math:: \frac{\omega_{1}S}{2kD}L_{1}=\frac{\omega_{2}S}{2kD}L_{2}

.. math:: \frac{\omega_{1}}{\omega_{2}}=\frac{L_{2}}{L_{1}}

With :math:`\omega_{1}=14\omega_{2}` and :math:`L_{1}=500\,\mathrm{m}`, we have :math:`L_{2}=14L_{1}=7000\,\mathrm{m}`.

--------------

Question 2: Characteristic time of groundwater systems
------------------------------------------------------

In class we discussed the somewhat complicated solution by series expansion of the evolution of the head after a sudden rain shower of :math:`P` [m] in a strip of land of width :math:`L` [m] between parallel fixed-head boundaries with water level :math:`\phi_{0}` [m]. We have seen that after some time :math:`t` [d], only the first term matters, which is

.. math:: s\left(x,t\right)=\phi\left(x,t\right)-\phi_{0}=\frac{P}{S_{y}}\frac{4}{\pi}\cos\left(\pi\frac{x}{L}\right)\exp\left(-\pi^{2}\frac{kD}{L^{2}S_{y}}t\right)

Whenever possible express your answers mathematically:

#.   What is the shape of the head?

--------------

A cosine

--------------

What is the maximum head, take :math:`\phi_{0}=0`?

.. math:: s\left(0,t\right)=\frac{P}{S_{y}}\frac{4}{\pi}\exp\left(-\pi^{2}\frac{kDt}{L^{2}S_{y}}\right)

#. What would you consider the characteristic time of this system?

--------------

The most suitable definition may be this:

.. math:: T=\frac{L^{2}S}{\pi^{2}kD}

Because it reduces the formula for the maximum head to:

.. math:: s\left(0,t\right)=\frac{P}{S_{y}}\frac{4}{\pi}\exp\left(-\frac{t}{T}\right)

One could also choose another definition like

.. math:: T=\frac{L^{2}S}{4kD}=\frac{b^{2}S}{kD}

Which may be better memorizable. It turn the formula into

.. math:: s\left(0,t\right)=\frac{P}{S_{y}}\frac{4}{\pi}\exp\left(-\frac{\pi^{2}}{4}\frac{t}{T}\right)

--------------

#. What would be the half-time of this groundwater system?

--------------

The half-time is the time it takes for something to become half as large. For exponential declining systems this is a constant. This is the case here with the head relative to its final value. Let the half-time be , then we can formally express the half-time as the time it takes such that the ratio of the head at time is half the head at time :

.. math:: \exp\left(-\xi\left(\frac{t+T_{50\%}}{T}\right)\right)=0.5\exp\left(-\xi\left(\frac{t}{T}\right)\right)

.. math:: -\xi\left(t+T_{50\%}\right)=-T\ln2-\xi t

.. math:: T_{50\%}=\frac{\ln2}{\xi}T

where :math:`\xi` follows from the expression under the exponent, and threfore, from the definition of the characteristic time.

--------------

Question 4: Wells
-----------------

The solution by Theis is given by

.. math:: s\left(r,t\right)=\phi_{0}-\phi\left(r,t\right)=\frac{Q_{0}}{4\pi kD}\mathrm{W}\left(u\right)\mbox{, where }u=\frac{r^{2}S}{4kDt}

#. What flow conditions are described by Theis’ well solution?

--------------

The Theis solution describes the drawdown due to a well in a confined (constant :math:`kD`) aquifer extracting a flow :math:`Q_{0}` from :math:`t=0`.

--------------

#. What are its parameters and what are their dimensions?

--------------

:math:`s`:
   [L] drawdown; [m] head relative to fixed datum

:math:`Q_{0}`:
   [L\ :sup:`3`/T] is the constant extraction from the well.

:math:`kD`:
   [L\ :sup:`2`/T] aquifer transmissivity

:math:`u`:
   [-] argument of well function

:math:`r`:
   [m] distance from well

:math:`S`:
   [-] storage coefficient of aquifer :math:`S_{y}`\ or :math:`S_{S}D`

:math:`t`:
   [T] time since the well started its extraction.

--------------

As you know, the function W(:math:`u`) is the exponential integral, which may be written as a series expansion :

.. math:: \mathrm{W}\left(u\right)=-0.577316-\ln u+u-\frac{u^{2}}{2\times2!}-\frac{u^{3}}{3\times3!}+\frac{u^{4}}{4\times4!}\cdots

#. How can you mathematically approximate the Theis’ solution for very small values of :math:`u` given that :math:`-0.577216\approx\ln\left(0.5615\right)`?

--------------

For sufficiently small :math:`u` we may truncate all terms above :math:`\ln u` in the series expression, to get

.. math:: \mathrm{W}\left(u\right)\approx-0.577361-\ln u\mbox{, where }u=\frac{r^{2}S}{4kDt}

Fill in :math:`u` into the formula to obtain

.. math:: \mathrm{W}\left(u\right)\approx\frac{2.3Q}{4\pi kD}\log\left(\frac{2.25kDt}{r^{2}S}\right)

--------------

#. With this approximation, mathematically give the difference between the drawdown obtained at time t and the drawdown at time 10t in a piezometer at some arbitrary distance r from the well.

--------------

.. math:: s_{10t}-s_{t}=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kD\left(10t\right)}{r^{2}S}\right)-\log\left(\frac{2.25kDt}{r^{2}S}\right)\right]=\frac{2.3Q}{4\pi kD}

--------------

#. Also give the difference between the drawdown in a piezometer at distance r from the well and in a piezometer at distance 10r from the well, both at the same time.

.. math:: s_{10t}-s_{t}=\frac{2.3Q}{4\pi kD}\left[\log\left(\frac{2.25kDt}{r^{2}S}\right)-\log\left(\frac{2.25kDt}{10^{2}r^{2}S}\right)\right]=\frac{2.3Q}{4\pi kD}\log\left(10^{2}\right)=\frac{2.3Q}{2\pi kD}

Closed-book exam (1h), Feb 5, 2010
==================================

.. _question-1-9:

Question 1:
-----------

#. What is liquefaction?

--------------

Loosely packed fine sand may become liquefied and turn into quicksand by a shock (earthquake) by which grains become untached, the matrix tries to resettle into a more compact configuration, but the water cannot escape immediately due to the small conductivity of the fine sand.

--------------

#. What is the difference between specific yield and elastic storage?

--------------

Water table storage versus storage due to the elastic properties of both the water and the matrix.

--------------

#. How does the specific yield change if an already shallow water table rises?

--------------

In a phreatic aquifer with a shallow water table, specific yield gets smaller the shallower the water table. This is due to the moister profile intersecting ground surface. See syllabus,

--------------

#. Why does this happen (make a sketch and explain)?

--------------

See syllabus page 12.

--------------

#. Which of the two materials, gravel and fine sand, has the highest specific yield and why (assume both have the same porosity)?

--------------

The coarser material has the highest specific yield because it has the lowest specific retention, because less water can adhere against gravity in the unsaturated zone because of the much smaller specific surface in each volume of coarse material than the same volume of fine material.

--------------

.. _question-2-7:

Question 2:
-----------

The head in an aquifer connected to the ocean fluctuates due to tide. This fluctuation is given by the following formula, in which *s* expresses the head variation caused by the tide as a function of time *t* and the inland distance from the shore *x*:

   .. math:: s\left(x,t\right)=A\,\exp\left(-ax\right)\sin\left(\omega t-ax\right)\mbox{, with }a=\sqrt{\frac{\omega S}{2kD}}

#. What is the expression for the maximum head fluctuation as a function of *x*?

This expression is just the part of the tide formula without the sine:

--------------

.. math:: s\left(x,t\right)=A\,e^{-ax}

--------------

#. Sketch the head change s as a function of x at time t=0 and sketch also the envelope (maximum and minimum value of s as a function of x)

.. container:: centering

   .. figure:: pictures/2010_0.png
      :alt: Sketch of wave as a function of :math:`x`
      :width: 80.0%

      Sketch of wave as a function of :math:`x`

#. Which parameters increase the inland penetration of the tide and which parameters decrease this inland penetration?

--------------

Parameters increasing the penetration depth of the tide wave are those that reduce the value of the damping alfa, that is a lower frequency omega, a lower storage coefficient and a higher transmissivity.

--------------

.. _question-3-8:

Question 3:
-----------

Consider an extraction canal in direct contact with an aquifer of infinite extent. The aquifer has transmissivity :math:`kD=400\,\mathrm{m^{2}/d}` and specific yield :math:`S_{y}=0.1`. As long as :math:`t<0`, the head in the aquifer is everywhere 0 m (we take the initial water level as our reference level).

At time :math:`t=0\,\mathrm{d}`, the water level in the canal suddenly changes to 2 m. Then, at time :math:`t=2~\mathrm{d}`, the water level in the canal suddenly changes back to its original value of 0 m and remains constant afterwards.

The head change and the head-change gradient are:

.. math:: s=s_{0}\mathrm{erfc}\left(\sqrt{\frac{x^{2}S}{4kDt}}\right)\mbox{ and }\frac{\partial s}{\partial x}=-s_{0}\sqrt{\frac{S}{\pi kDt}}\exp\left(-\frac{x^{2}S}{4kDt}\right)

To obtain values for the **:math:`\mathrm{erfc}`** function, use the graph below.

Answer the following two questions.

#. Compute the head at :math:`x=100\,\mathrm{m}` at :math:`t=3\,\mathrm{d}`. Show the formula you use and include the dimension in your answer!

--------------

This problem is solved by superposition in time:

.. math:: s=s_{0}\mathrm{erfc\left(\sqrt{\frac{x^{2}S}{4kDt}}\right)-s_{0}\mathrm{erfc}\left(\sqrt{\frac{x_{2}S}{4kD\left(t-3\right)}}\right)}

Fill in the numbers to get your answer.

--------------

#. Compute the discharge at :math:`x=0` at :math:`t=3\,\mathrm{d}`. Show the formula you use and include the dimension in your answer?

--------------

The discharge at x=0 as a function of time equals

.. math:: q\left(0,t\right)=-kD\frac{\partial s}{\partial x}=-kDs_{0}\sqrt{\frac{S}{\pi kDt}}

so,

.. math:: q\left(0,3\right)=s_{0}\sqrt{\frac{kDS}{\pi}}\left(\sqrt{\frac{1}{t}}-\sqrt{\frac{1}{t-3}}\right)=2\sqrt{\frac{400\times0.1}{\pi}}\left(\sqrt{\frac{1}{3}}-\sqrt{\frac{1}{3-1}}\right)=-3.02\,\mathrm{m^{2}/d}

--------------

.. container:: centering

   .. figure:: pictures/2010_1.png
      :alt: Function :math:`\mathrm{erfc}\left(u\right)`
      :width: 70.0%

      Function :math:`\mathrm{erfc}\left(u\right)`

Quesiton 4:
-----------

Consider a well in a system of infinite extent which starts extracting at time *t*\ =0. We know that Theis’ formula applies:

.. math:: s\left(r,t\right)=\frac{Q}{4\pi kD}\mathrm{W}\left(u\right)\mbox{, where }u=\frac{r^{2}S}{4kDt}

We also know that for small values of *u*, the well function, W(:math:`u`), can be approximated by a straight line on log-t scale, which is given by:

.. math:: \mathrm{W}\left(u\right)\approx2.3\log\left(\frac{0.5625}{u}\right)=2.3\log\left(\frac{2.25kDt}{r^{2}S}\right)

Consider a pumping test on this well, starting the constant extraction :math:`Q=800\,\mathrm{m^{3}/d}` at :math:`t=0`. The drawdown is measured over a number of days at an observation well at 25 m distance. The measured drawdowns are shown in the figure below, which clearly reveals the straight portion of the drawdown that we expect from the expression above for large-enough values of time.

#. Using the straight line through the measured data, compute the transmissivity *:math:`kD`* and the storage coefficient *:math:`S`* of this aquifer.

--------------

The drawdown difference per log cycle is the most convenient way to compute the transmissivity. First draw a line through the straight portion of the graph (see figure below) and then measure the drawdown increase per log cycle, which is about 0.32 m. Then with log(10)=1, compute the transmissivity from

.. math:: s_{10t}-s_{t}\approx\frac{2.3Q}{4\pi kD}\rightarrow kD=\frac{2.3Q}{4\pi\left(s_{10t}-s_{t}\right)}=\frac{1.3\times800}{4\pi0.32}\approx460\,\mathrm{m/d}

Next we get the storage coefficient from the point where the straight drawdown line of the above expression is zero, which is at about 0.12 days:

.. math:: \frac{2.25kDt}{r^{2}S}=1\rightarrow S=\frac{2.25kDt}{r^{2}}=\frac{2.25\times460\times0.12}{25^{2}}\approx0.2

--------------

.. container:: centering

   .. figure:: pictures/2010_2.png
      :alt: Measured drawdown during pumping test.
      :width: 80.0%

      Measured drawdown during pumping test.

Closed-book exam (3h), Feb 2009
===============================

.. _question-1-10:

Question 1:
-----------

#. What is the difference between specific yield and elastic storage?

--------------

Storage coefficient in respectively unconfined and (semi)-confined aquifers.

--------------

#. How does the specific yield change if an already shallow water table rises further and becomes even shallower?

--------------

The specific yield becomes smaller.

--------------

#. Why does this happen (make a sketch and explain)?

--------------

Part of the unsaturated profile that would store or yield water now extends above ground surface, and no longer exists so that it cannot contribute to storage.

--------------

#. Which of the two materials, gravel and fine sand, has the highest specific yield and why (assume both have the same porosity)?

--------------

Fine sand, due to its much larger surface area and number contact points between grains.

--------------

.. _question-2-8:

Question 2:
-----------

#. What do we mean by Loading Efficiency (:math:`LE`) and what do we mean by Barometric Efficiency (:math:`BE`)?

--------------

:math:`LE` is the portion of the increased total pressure supported by the water and increasing the head.

The :math:`BE` is the portion of the barometric pressure change causing change of head.

Both :math:`LE` and :math:`BE` only work in (semi)-confined aquifers.

--------------

#. What is the difference in terms of head change if we compare a loading on land surface with an equal increase of the barometer pressure? And why?

--------------

In case of a load change, the head changes in the same direction ad the load, with barometric change it changes in the opposite direction. An increase of barometric pressure caused a decrease in head.

The difference is due to the face that the barometric pressure also works in the piezometer, while a load increase does not.

--------------

.. _question-3-9:

Question 3:
-----------

Tidal flow in a confined aquifer may be described mathematically by

.. math:: s=A\,e^{-ax}\sin\left(\omega t-ax\right)\mbox{, where }a=\sqrt{\frac{\omega S}{2kD}}

#. What are the different quantities in these expressions and what are their dimensions?

--------------

:math:`s`:
   head change due to the wave at :math:`x=0` [m]

*:math:`A`:*
   is amplitude of tide [m]

:math:`a`:
   is dampoing factor [1/m]

:math:`\omega`:
   is tidal frequency[radians/day]

*:math:`S`:*
   [-] is storage coefficient [-]

*:math:`kD`:*
   is transmissivity. [m\ :math:`^{2}`/d]

--------------

#. By what expression is the envelope given (the envelope describes the maximum amplitude as a function of :math:`x`?)

--------------

.. math:: A_{x}=A_{0}\,e^{-ax}

--------------

#. How does the envelope change if the frequency of the tide would double?

It is reduced. Less penetration of the wave into the aquifer as follows from.

.. math:: \frac{A_{x}}{A_{0}}=\exp\left(-\sqrt{\frac{\omega S}{2kD}}x\right)

#. How will the envelope change if the transmissivity would be two times less and the storage coefficient 100 times less?

The damping factor is

.. math:: a=\sqrt{\frac{\omega S}{2kD}}

The larger :math:`a` the more damping and the less penetration of the wave into the aquifer. A higher :math:`\omega` (frequency) increase the damping. :math:`\omega=0` implies the lowest possible frequency, which yields no damping, and, therefore the same :math:`s` independent of :math:`x`, which is equivalent to the steady stat situation. The damping is also increased with higher :math:`S` and with lower :math:`kD`.

.. _question-4-3:

Question 4:
-----------

The picture below shows a strip of land of width *L* bounded by two canals. Both the strip and the canals run perpendicular to the paper (so the picture is a cross section). Suddenly the water level in the left canal is raised by *A* m as is indicated in the figure. This causes the head to change in the strip. At the right hand side the water level is unchanged. There exists an expression, which mathematically describes the effect of a sudden level rise in a strip that is unbounded on one side. We want to use this expression to computed the head in the strip. We can do this by means of mirror canals.

.. container:: centering

   .. figure:: pictures/2009_1.png
      :alt: Strip of land of width *L* bounded by open water. The water level at the left hand side was suddenly raised by *A* m. This causes the head in the aquifer of the strip to change dynamically.
      :width: 100.0%

      Strip of land of width *L* bounded by open water. The water level at the left hand side was suddenly raised by *A* m. This causes the head in the aquifer of the strip to change dynamically.

#. Irrespective of what the mathematical looks like, where would you put the mirror canals and which are positive and which are negative? Just draw an arrow respectively up or down (see figure) at the locations where you would put the mirror canal.

.. container:: centering

   .. figure:: pictures/2009_2.png
      :alt: Same as previous figure, but now with superposition scheme shows by the arrows.
      :width: 100.0%

      Same as previous figure, but now with superposition scheme shows by the arrows.

Question 5:
-----------

The characteristic dynamics of a groundwater systems (i.e., the time it takes for the head of a groundwater system to reach equilibrium) is related to the argument of transient groundwater flow solutions, This argument is :math:`\sqrt{\frac{x^{2}S}{4kDt}}` in solutions for one-dimensional flow and :math:`\frac{r^{2}S}{4kDt}` for radial flow such as in the well functions of Theis and Hantush.

#. Explain how the characteristic dynamics relate to these arguments?

--------------

In a system of given width :math:`L` the factor :math:`T=\frac{L^{2}S}{4kDt}` has dimension time and is directly related to the dynamics of a groundwater basin. It can be considered the characteristic time of the basin/system.

--------------

#. Compare the characteristic dynamics of two systems. System two is twice as wide as system one and its transmissivity is 3 times as large and its storage coefficient 100 times as small as that of system one. How do the dynamics of these two systems relate to each other, that is: how many times faster or slower is system two compared to system one in reaching piezometric equilibrium?

The factor :math:`T=\frac{L^{2}S}{4kDt}` with dimensions time is a measure for the characteristic time of the groundwater system. System #2 thus has a characteristic time that is :math:`2^{2}\times0.01/3=0.013\approx1/75` times larger or 75 times smaller than system #1.

Question 6:
-----------

Consider a well in a semi-confined aquifer with :math:`kD=900\,\mathrm{m^{2}/d}`, :math:`S=0.001` and :math:`c=400\,\mathrm{d}` that is pumped at a discharge :math:`Q=2400\,\mathrm{m^{3}/d}`.

#. How long does it take before the drawdown at 60 m distance from the well becomes stationary?

.. math:: \lambda=\sqrt{kDc}=\sqrt{900\times400}=600\,\mathrm{m}\rightarrow\frac{r}{\lambda}=\frac{60}{600}=0.1

See where the Hantush type curve for :math:`r/\lambda=0.1` becomes horizontal (stationary). Read the :math:`1/u` value, which is about 1000, and compute the time.

.. math:: \frac{1}{u}=\frac{4kDt}{r^{2}S}\rightarrow t=\frac{r^{2}S}{4kDu}=\frac{60^{2}\times0.001}{4\times900}\times1000\approx1.0\,\mathrm{d}

#. What is the final drawdown?

This drawdown, because it is steady state can be computed either by the De Glee formula (with the Bessel Function) or with the Hantush formula

.. math:: s=\frac{Q}{2\pi kD}\mathrm{K_{0}}\text{\ensuremath{\left(\frac{r}{\lambda}\right)}=\ensuremath{\frac{Q}{4\pi kD}\mathrm{W}\left(u,\frac{r}{\lambda}\right)}}

This is true, because the flow is steady state.

Using the type curves given we apply Hantush which yields with :math:`1/u=100`\ 0 and :math:`r/L=0.1`, :math:`\mathrm{W\left(\cdots\right)}=1.9`, so

.. math:: s=\frac{2400}{4\pi900}1.9\approx0.4\,\mathrm{m}

Quesiton 7:
-----------

A pumping test has been carried out in a confined aquifer. The drawdown and the Theis type curves are given in the graphs below. Theses graphs have been drawn on the same type of double logarithmic paper. The extraction of the well during the test was 1000 m\ :sup:`3`/d. Determine the transmissivity and the storage coefficient of this groundwater system.

.. container:: centering

   .. figure:: pictures/2009_3.png
      :alt: Theis well function Type curve.
      :width: 80.0%

      Theis well function Type curve.

.. container:: centering

   .. figure:: pictures/2009_4.png
      :alt: Measured drawdown versus :math:`t/r^{2}.`
      :width: 80.0%

      Measured drawdown versus :math:`t/r^{2}.`

.. container:: centering

   .. figure:: pictures/2009_5.png
      :alt: Theis and Hantush well function type curves.
      :width: 80.0%

      Theis and Hantush well function type curves.

--------------

Fold the paper and tear off the lower graph. Shift the two graphs over each other until they match (keep axes parallel). Then choose a “match point” and read the combined value of :math:`s` and :math:`\mathrm{W}` to obtain :math:`kD` from

.. math:: s=\frac{Q}{4\pi kD}\mathrm{W\rightarrow kD=\frac{Q}{4\pi s}\mathrm{W}}

With numbers read from both graphs once overlaid (:math:`\mathrm{W}=1` and :math:`s=0.1\,\mathrm{m}`)

.. math:: kD=\frac{Q}{4\pi S}\mathrm{W}=\frac{1000}{4\pi0.1}\times1\approx795\,\mathrm{m/d}

Then read the combined values of :math:`1/u` and :math:`t/r^{2}` from the graphs and determine :math:`S/kD` from

.. math:: \frac{1}{u}=\frac{4kD}{S}\frac{t}{r^{2}}\rightarrow\frac{S}{kD}=4u\frac{t}{r^{2}}

In numbers with :math:`1/u\approx1.0` and :math:`t/r^{2}\approx3\times10^{-7}` we get

.. math:: \frac{S}{kD}=4u\frac{t}{r^{2}}=4\times1\times3\times10^{-7}=1.2\times10^{-6}\,\mathrm{d/m^{2}}

Finally compute :math:`S=1.2\times10^{-6}\times kD=1.2\times10^{-6}\times795\approx10^{-3}`.

--------------

Closed-book exam (3h), Feb 2007
===============================

Question 1: Conceptual
----------------------

#. What is specific yield?

--------------

Specific yield, :math:`S_{y}`, is the reversible storage caused by filling and emptying of pores. Hence, it is the storage coeffiicent for the phreatic or water-table aquifer.

--------------

#. How does specific yield depend on the distance of the water table below ground level?

--------------

The shallower the water table above some depth, the lower the specific yield. This is due to the moisture curve intersecting ground surface, due to which the contents below the remaining moisture curve is less than when it does not intersect ground surface.

--------------

#. What happens to the water table in a piezometer in a confined aquifer when the barometer pressure goes up, why?

--------------

The water table goes down by the amount of the increased (changed) barometer pressure (divided by :math:`\rho g` of course, to convert from pressure to water column) that is not supported by the aquifer grain matrix.

--------------

Question 2: Diffusion equation
------------------------------

The diffusion equation for transient flow in one dimension is :math:`D\frac{\partial^{2}s}{\partial x^{2}}=\frac{\partial s}{\partial t}`

#. What is the dimension of the diffusivity *D*?

--------------

It’s always [L\ :math:`^{2}`/T]. (This follows immediately from the partial differential equation.)

--------------

#. What is diffusivity *D* in the case of groundwater flow?

--------------

Ease of flow divided by storage, hence :math:`kD/S`.

--------------

#. What is diffusivity *D* in the case of heat flow?

--------------

Ease of flow divided by strorage, hence, :math:`\frac{\lambda}{\rho c}`, i.e., head conductance over specific head capacity

.. math:: \frac{\lambda}{\rho c}=\mathrm{[\frac{E}{TL^{2}}/(\frac{K}{L})]/[\frac{M}{L^{3}}\frac{E}{MK}]=[L^{2}/T],\,e.g.,\,m^{2}/s,\,mm^{2}/s\,etc}.

--------------

Question 3: Fluctuation groundwater
-----------------------------------

In the case of a tidal fluctuation in a river in direct contact with an aquifer having transmissivity the fluctuation of the head may be described by

.. math:: s=s_{0}\exp\left(-ax\right)\sin\left(\omega t-ax\right)\mbox{, with }a=\sqrt{\frac{\omega S}{2kD}}

#. What is *:math:`s`* and what does this function look like? Make a sketch of *s* as a function of *x*, and show its envelopes. (The envelope is the curve of the values between which the function fluctuates, as a function of :math:`x`).

--------------

Lowercase *:math:`s`* [m] is the head change that is only due to the wave (driven by the given fluctuation at :math:`x=0`. The function is a damped sine wave, i.e. it fluctuatuates between its envelopes defined by :math:`\pm A\exp(-ax)`.

--------------

#. In the case of a double-day tide, :math:`\omega=\frac{4\pi}{24}\,\mathrm{h^{-1}}`, what would be the speed of the wave into the aquifer if :math:`S=0.001` and :math:`kD=500\,\mathrm{m^{2}/d}`? (Notice the dimensions!)

--------------

The speed of the wave follows from keeping the argument of the sine constant. This leads to the expression :math:`\omega t-ax=\mathrm{const}`. To get the velocity, differentiate with respect to *t* to get :math:`\omega-a\frac{dx}{dt}=0`, to :math:`v=\frac{dx}{dt}=\frac{\omega}{a}`. At what distance from the river is the amplitude of the head fluctuation still only half of that in the river at :math:`x=0`?

--------------

#. What happens to this distance in case the transmissivity would be 9 times a big?

--------------

Note that :math:`a=\sqrt{\frac{\omega S}{2kD}}`. Hence a 9 times larger :math:`\text{\ensuremath{kD}}` causes a 3 times lower value of the damping factor ‘\ :math:`a`\ ‘ and so, a 3 times higher velocity of the wave.

--------------

Question 4: Flow to an extraction canal
---------------------------------------

Consider an extraction canal in direct full contact with an aquifer with transmissivity :math:`kD=400\,\mathrm{m^{2}/d}` and specific yield :math:`S_{y}=0.1`. The water level in the canal suddenly changes by 2 m downward. The head and gradient are given by:

.. math:: s=s_{0}\mathrm{erfc}\left(\sqrt{\frac{x^{2}S}{4kDt}}\right)\mbox{ and }\frac{\partial s}{\partial x}=-s_{0}\sqrt{\frac{S}{\pi kDt}}\exp\left(-\frac{x^{2}S}{4kDt}\right)

#. Compute the discharge into the canal after 1d. Show the formula you use and include the dimension in your answer!

--------------

Easy, just fill in the numbers.

--------------

#. What is the head change *:math:`s`* at 100 m from the canal after 1 and after 2 d? (Use erfc-curve further down).

--------------

Just fill in the numbers after reading the right values from the curve of the erfc-function.

--------------

#. What is the head change at 100 m from the canal after 2 days if the head in the river would change back by 2 m at :math:`t=1\,\mathrm{d}`?

--------------

This requires superposition. Let the effect of the sudden head change at t=0 continue forever and subtract the effect of the sudden head change occurring at :math:`t=2\,\mathrm{d}` forever.

--------------

Question 5: Well in semi-confined aquifer
-----------------------------------------

Consider a transient well in a semi0-confined aquifer so that Hantush’s solution is valid, hence,

.. math:: s=\frac{Q}{4\pi kD}\mathrm{W}\left(u,\frac{r}{\lambda}\right)\mbox{, with }u=\frac{r^{2}S}{4kDt}\mbox{ and }\lambda=\sqrt{kDc}

with :math:`kD=600\,\mathrm{m^{3}/d}`, :math:`c=900\,\mathrm{d}`, :math:`S=0.001` and pumping at a rate :math:`Q=2400\,\mathrm{m^{3}/d}`.

#. How long does it take before steady state is reached for a point at *r*\ =300 m from the well (why)? Use Hantush type curves (see graphic at the end of this exam).

--------------

Compute :math:`r\text{/}\lambda` and look in the curve below when the line for this value becomes horizontal, therefore, steady state. Use the corresponding value of :math:`1\text{/}u` which is :math:`4kDt\text{/}\left(r^{2}S\right)`, fill in the know values of :math:`\text{\ensuremath{kD}}`, :math:`r` and :math:`S` and compute the time :math:`t`

--------------

Question 6: Drawdown due to a pumping station in an unconfined aquifer
----------------------------------------------------------------------

A well is situated at 100 m from an impermeable infinitely long wall. The well is pumping at a rate of 2400 m\ :sup:`3`/d. Even though the aquifer is unconfined, the transmissivity *:math:`kD`* may be taken as a constant equal to 600 m\ :sup:`2`/d, while the specific yield *:math:`S_{y}`* equals 0.2. The well bore has a radius of :math:`r_{0}=0.25\,\mathrm{m}`.

#. What is the drawdown at the well bore after 10 days of pumping ?

--------------

The wall is impermeable, so we must place a mirror well with the same pumping rate at 100 m beyond the wall to compute the drawdown. The drawdown is then obtained by the superposition of the well and its mirror well:

.. math:: s(0.25,t)=\frac{Q}{4\pi\text{kD}}\left(W_{h}\left(\frac{0.25^{2}S}{4\text{kDt}},\frac{0.25}{\lambda}\right)+W_{h}\left(\frac{200^{2}S}{4\text{kDt}},\frac{200}{\lambda}\right)\right)

Just fill in the numbers for :math:`\text{kD}`, :math:`S`, :math:`\lambda=\sqrt{\text{kDc}}` and :math:`t`\ =10 d, look up the value for :math:`W_{h}\left(u,\frac{r}{\lambda}\right)` in the graph and compute the answer.

--------------

#. A well in a confined aquifer of infinite extent, with :math:`kD=1000\,\mathrm{m^{2}/d}` and :math:`S=0.001`, is pumping at a rate of :math:`Q=24000\,\mathrm{m^{3}/d}`. How far would the radius of influence of this well after 100 years? The radius of influence is the radius beyond which the drawdown is considered negligible. You may exploit the logarithmic approximation of the Theis well function for large times:

.. math:: \mathrm{W}\left(u\right)\approx\ln\left(\frac{0.5625}{u}\right)\mbox{, with }u<0.1\mbox{ and }u=\frac{r^{2}S}{4kDt}

by making it zero.

The long-term drawdown in a confined aquifer due to a well pumping from :math:`t=0` at a constant rate is given by the Theis equation, which approaches a logarithmic function for large enough times (see given formula of :math:`\mathrm{W}(u)`). A practical approximation of the area of influence is where this approximation of the Theis solution, hence, the linear drawdown on half-log paper is zero. This is mathematically done by setting the argument of the log equal to 1. Hence,

.. math:: \frac{0.5625}{u}=\frac{0.5625\times4kDt}{r^{2}S}=1\mbox{, and, therefore, }r=\sqrt{\frac{2.25kDt}{S}}

.. container:: centering

   .. figure:: pictures/2007_1.png
      :alt: :math:`\mathrm{erfc}\left(u\right)`\ function.
      :width: 80.0%

      :math:`\mathrm{erfc}\left(u\right)`\ function.

.. container:: centering

   .. figure:: pictures/2007_2.png
      :alt: Theis and Hantush type curves. In case this graph is copied in black and white only, note that the lowest type curve is for the highest value of *:math:`r/\lambda`.* Note that the :math:`L` in the title and left axis of this figure stands for :math:`\lambda=\sqrt{kDc}` value
      :width: 80.0%

      Theis and Hantush type curves. In case this graph is copied in black and white only, note that the lowest type curve is for the highest value of *:math:`r/\lambda`.* Note that the :math:`L` in the title and left axis of this figure stands for :math:`\lambda=\sqrt{kDc}` value

Closed-book exam (3h) Feb 2006
==============================

.. _question-1-conceptual-1:

Question 1: Conceptual
----------------------

#. What types of reversible storage do you know in aquifer systems, explain how it works

--------------

Pore-water storage (by filling and emptying of pores) know as specific yield, and elastic storage by compression and expansion of the aquifer matrix and the water. Note that when the water pressure increases, the pore matrix expands while the water is compressed.

--------------

#. What values may you expect for the respective storage coefficients?

--------------

Specific yield values will range between a few percent to around 25% depending on the pore space and for very fine pores also on the time scale at which the head or water table varies. Elastic storage will be in the order of 10e-3 depending on the natural stress of the aquifer and its thickness, and the specific storage coefficient in the order of 10e-5/m mainly depending on the natural stress on the grains.

--------------

#. What is barometric efficiency, explain how it works.

--------------

The barometric efficiency, :math:`BE`, is the fraction of the barometer pressure change that will cause drawdown in a (semi) confined aquifer. The barometer pressure change is partly taken up by the aquifer matrix (the loading efficiency :math:`\text{\ensuremath{LE}}`) while the rest of supported by a change in head (the barometric efficiency :math:`\text{\ensuremath{BE}}`). The essence is :math:`BE+LE=1`.

--------------

#. When the barometric pressure increases, does the head (water table in a piezometer) in the confined aquifer rise or fall?

--------------

It falls, because the water pressure in the aquifer increases by the part not supported by the grains, i.e., by :math:`\text{LE}\times p_{a}` while the barometer pressure presses with full :math:`p_{a}` on the water surface in the piezometer. Hence its level must decline by :math:`p_{a}(1-LE)\text{/}(\rho g)` to keep pressure equilibrium.

--------------

#. Between what values may the barometric efficiency vary?

--------------

Between 960 and 1040 hPa, or about 9.6 and 10.4 m water column.

--------------

#. What happens in a confined aquifer with the head if a load is suddenly placed on ground surface, such as a train stopping near a piezometer? What happens when it leaves? Sketch a graph showing the head versus time that you would expect in that case.

--------------

The head increases initially with about :math:`\text{\ensuremath{LE}\ }\Delta p` where :math:`\Delta p` is the pressure increase in the aquifer due to the train arriving. The pressure then drops off as the local head increase below the train causes the groundwater to flow away so that after a while the head is the same as before. The opposite happens when the train leaves.

--------------

Question 2: Characteristic time of groundwater basin
----------------------------------------------------

Characteristic time of groundwater basin, the partial differential equation of which reads

.. math:: kD\frac{\partial^{2}\phi}{\partial x^{2}}=S\frac{\partial\phi}{\partial t}

#. What is a characteristic time of a groundwater basin that may be considered as one-dimensional of characteristic size *L*? (hint: Make partial differential equation dimensionless by setting :math:`\xi=\frac{x}{L}`, :math:`\tau=\frac{t}{T}` and see what :math:`T` is.

--------------

The partial differential equation will then be converted into

.. math:: \frac{kD}{L^{2}}\frac{\partial\phi^{2}}{\partial\xi^{2}}=\frac{S}{T}\frac{\partial\phi}{\partial\tau}

or

.. math:: \frac{\partial\phi^{2}}{\partial\xi^{2}}=\frac{L^{2}S}{\text{kDT}}\frac{\partial\phi}{\partial\tau}

So that setting :math:`\frac{L^{2}S}{kDT}=1` gives that :math:`T=\frac{L^{2}S}{kD}` can be considered a characteristic time of the groundwater system of size :math:`L` (with :math:`L` the approximate distance between opposite head boundaries (distance between local reivers for instance).

--------------

#. To reach equilibrium, how many times slower is a large basin compared to a small one with the same transmissivity and storage coefficient?

--------------

The size of the basin as measured by :math:`L` is squared in the characteristic time. So, a basin where the :math:`L` is 5 times as large as another basin is 25 times a slow in its drainage (natural drainage to equilibrium)

--------------

#. Compute the characteristic time for the following cases:

   --------------

   Large basin: *kD*\ =500 m\ :sup:`2`/d, system width *L*\ =100km, storage coefficient *S*\ =0.2,

   .. math:: T=\frac{\left(10^{5}\right)^{2}\times0.2}{100}=2\times10^{7}\,d=\text{many},\text{many}\,\text{years}

   --------------

--------------

Small basin: *kD*\ =100 m\ :sup:`2`/d, system width *L*\ =100m , storage coefficient *S*\ =0.1

.. math:: T=\frac{100^{2}\times0.1}{100}=10\,d

--------------

Quesiton 3: Tides in groundwater
--------------------------------

   Given: The tidal fluctuation in an aquifer in a point at distance *x* from the sea due to the water level fluctuation at sea with amplitude *A* is described by the following formula

   .. math:: s\left(x,t\right)=A\,\exp\left(-ax\right)\sin\left(\omega t-ax\right)

   in which the damping factor is as follows :math:`a=\sqrt{\frac{\omega S}{2kD}}`, where :math:`\omega` is the angle velocity in radians/time or :math:`\omega=\frac{2\pi}{T}` where :math:`T` is the time of a complete wave cycle.

Are the following expressions true or false?

#. The wave in the aquifer has a different frequency than the tide itself.

--------------

False, it’s physically unimaginable that the frequencies would be different.

--------------

#. The amplitude of the wave at a given distance from the sea becomes greater when

--------------

The frequency of the tide is reduced?

The higher the frequency, so the higher :math:`\omega`, to higher the damping :math:`a` and, therefore, the smaller the distance over which the fluctuation in the

aquifer can be felt. Only an infinitely slow frequency reaches to infinity, as this is equivalent to the steady-state situation.

--------------

--------------

The storage coefficient is reduced?

The smaller the storage coefficient the faster and the farther the fluctuation travels inland. With a (theoretically) zero storage coefficient, the wave would (only theoretically) travel with infinite speed, which would imply that only a steady state situation would be possible (zero storage) or that the head at all :math:`x` would be the same as at :math:`x=0`.

--------------

--------------

Then the transmissivity is reduced?

The transmissivity determines ease of flow. Hence if reduces flow will be less easy. With zero transmissivity the fluctuation at zero would not penetrate the aquifer at all, speed zero; on the other hand, with transmissivity infinite, the speed of the wave would also be (theoretically) infinite and yield the same result as storage coefficient equal to zero.

--------------

Question 4: Aquifer with river
------------------------------

Consider an aquifer of infinite extent bounded by a fully penetrating river at :math:`x=0`. At :math:`t=0` the river level suddenly changes by a height :math:`A`. The change of head :math:`s(x,t)` in the aquifer equals in this case:

.. math:: s\left(x,t\right)=A\,\mathrm{erfc}\left(\sqrt{\frac{x^{2}S}{4kDt}}\right)

with :math:`\mathrm{erfc}(u)` as shown in the picture below

.. container:: centering

   .. figure:: pictures/2006_1.png
      :alt: :math:`\mathrm{erfc\left(u\right)}`\ versus :math:`u`
      :width: 80.0%

      :math:`\mathrm{erfc\left(u\right)}`\ versus :math:`u`

#. What is the final value of the head change (the value reached after infinite time, :math:`s\left(x,\infty\right)`?

--------------

That’s simple: it must be A, the new steady level of the river.

--------------

#. What value has the argument of :math:`\mathrm{erfc}(\cdots)`, i.e., :math:`\sqrt{\frac{x^{2}S}{4kDt}}` when the head change is half the final value?

--------------

From the graph it’s seen that it’s a fraction less than 0.5.

--------------

#. If :math:`kD=400\,\mathrm{m^{2}/d}`, :math:`S=0.1` and :math:`x=100\,\mathrm{m}`, after how much time is this the change of head equal to :math:`0.5A`?

--------------

This implies that the argument must be about 0.5, i.e.

.. math:: \frac{x^{2}S}{4\text{kDt}}=0.25

Just fill in :math:`\text{\ensuremath{kD}}` and :math:`S` and compute :math:`t`.

--------------

#. What would be the formula if the head change occurred on time *:math:`t_{1}`* instead of time\ :math:`t=0`?

--------------

.. math:: s(x,t)=A\ \text{erfc}\left(\frac{x^{2}S}{4\text{kD}\left(t-t_{1}\right)}\right)\mbox{, where }t>t_{1}

Again, set the argument equal to 0.5 to compute t at which the drawdown at :math:`x` is equal to :math:`0.5\ A`.

--------------

#. How could you compute the head change at point *x* if the there was a sudden change of the river level of *A*\ :sub:`1` at time *t*\ =\ *t*\ :sub:`1` and another of *A*\ :sub:`2` at *t*\ =\ *t*\ :sub:`2`?

--------------

By superposition, in this case

.. math:: s(r,t)=A_{1}\text{erfc}\left(\frac{x^{2}S}{4\text{kD}\left(t-t_{1}\right)}\right)+A_{2}\text{erfc}\left(\frac{x^{2}S}{4\text{kD}\left(t-t_{2}\right)}\right)

--------------

Question 5: Well in a confined aquifer
--------------------------------------

Consider a well in a confined aquifer starting an extraction of :math:`Q=1200\,\mathrm{m^{3}/d}` at :math:`t=0`. :math:`kD=1000\,\mathrm{m^{2}/d}`, and :math:`S=0.001`. For this case the Theis solution applies:

.. math:: s=\frac{Q}{4\pi kD}\mathrm{W\left(u\right)\mbox{, with }}u=\frac{r^{2}S}{4kDt}

(See the type curve of Theis well function on a separate page).

#. Compute the head at :math:`r=20\,\mathrm{m}` after :math:`t=1\,\mathrm{d}`.

--------------

.. math:: s(20,1)=\frac{1200}{4\pi1000}\mathrm{W}\left(\frac{20^{2}\times0.001}{4\times1000\times1}\right)

Where the argument of :math:`\mathrm{W}` is :math:`u` for which :math:`\mathrm{W}` can be looked up in the type curve below.

--------------

#. The pump is switched off after 1 day. What is the head after 1.1 days at :math:`r=20\,\mathrm{m}`?

--------------

In that case we apply superposition. That is, we place another well at the same spot and switch it on with :math:`-Q` at :math:`t=1.1` days and add the two wells. In math:

.. math:: s(20,1.1)=\frac{Q}{4\pi kD}\left(\mathrm{W}\left(\frac{20^{2}S}{4kD\times1.1}\right)-\mathrm{W}\left(\frac{20^{2}S}{4kD\times(1.1-1.0)}\right)\right)

Where the first term requires :math:`t>0` and the second :math:`t>1.0` d.

--------------

Question 6: Well in a leaky aquifer
-----------------------------------

Consider a transient well in a leaky aquifer. :math:`kD=400\,\mathrm{m^{2}/d}`, :math:`c=400\,\mathrm{d}`, :math:`S=0.001`, so that the groundwater behaves according to Hantush’s transient well formula

.. math:: s=\frac{Q}{4\pi kD}\mathrm{W}\left(u,\frac{r}{\lambda}\right)\mbox{, with }\lambda=\sqrt{kDc}

#. How long does it take until the head at :math:`r=40\,\mathrm{m}` becomes steady state or virtually steady state? (Hint: look at the type curves to get u for which this is the case, note).

--------------

Compute :math:`\frac{r}{\lambda}=\frac{40}{\sqrt{kDc}}` and look for the corresponding type curve in the graph with the type curves for the Hantush well function. Look for which value of :math:`1/u` the curve becomes horizontal, take the value of :math:`1/u` for the point, compute u and apply this value in the formula for :math:`u`, from which the time follows.

--------------

Question 7: Well in an unconfined aquifer
-----------------------------------------

Consider a well in an unconfined aquifer for which the Theis-solution applies (see type curve hereafter. Further given a pumping test with an extraction of :math:`Q=600\,\mathrm{m^{3}/d}` during which drawdown measurements were made (see the graph with the small circles).

Interpret the test (that is: compute *kD* and *S*).

(Hint: if you can’t see through the paper make the type curve thicker using a pen and hold both curves up against a light or in the direction of a window).

--------------

Shift the curves on top of each other keeping the axes parallel until you obtain the best possible fit. Then for that chosen (by arbitrary point) read the corresponding values of :math:`1/u` and :math:`1\text{/}r^{2}` and of the drawdown :math:`s` and :math:`\mathrm{W}(u)`.

The from the formula for the drawdown

:math:`s=\frac{Q}{2\pi kD}\mathrm{W}(u)` with now a corresponding value of :math:`s` and :math:`\mathrm{W}(u)` known as well as :math:`Q` known, compute the transmissivity. Next, with a corresponding value for :math:`t\text{/}r^{2}` and :math:`1/u` known and :math:`kD` just compute we have :math:`\frac{4kD}{S}\frac{t}{r^{2}}=\frac{1}{u}` from which the storage coefficient, :math:`S`, follows. In the case of a semi-confined aquifer, the match by shifting the graphs should also provide the curve with a specific value of :math:`r\text{/}\lambda` that best fits the measurements. This implies that with r known and :math:`kD` just determined we now also get the resistance c from :math:`\lambda=\sqrt{kDc}`.

--------------

.. container:: centering

   .. figure:: pictures/2006_2.png
      :alt: Theis type curve, :math:`\mathrm{W}\left(u\right)` versus :math:`1/u`
      :width: 80.0%

      Theis type curve, :math:`\mathrm{W}\left(u\right)` versus :math:`1/u`

.. container:: centering

   .. figure:: pictures/2006_3.png
      :alt: Measured drawdown during pumping test versus *:math:`t/r^{2}`*)
      :width: 80.0%

      Measured drawdown during pumping test versus *:math:`t/r^{2}`*)

.. container:: centering

   .. figure:: pictures/2006_4.png
      :alt: Theis and Hantush type curves combined, i.e., :math:`\mathrm{W}\left(u\right)` and :math:`\mathrm{W}\left(u,\frac{r}{\lambda}\right)` vs :math:`1/u`.
      :width: 80.0%

      Theis and Hantush type curves combined, i.e., :math:`\mathrm{W}\left(u\right)` and :math:`\mathrm{W}\left(u,\frac{r}{\lambda}\right)` vs :math:`1/u`.

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElechemr(RPackage):
	"""Electrochemical Reactions Simulation

	Digital simulation of electrochemical processes.
             Each function allows for implicit and explicit solution of the differential equation using methods like Euler, Backwards implicit, Runge Kutta 4, Crank Nicholson and Backward differentiation formula as well as different number of points for derivative approximation. Several electrochemical processes can be simulated such as: Chronoamperometry, Potential Step, Linear Sweep, Cyclic Voltammetry, Cyclic Voltammetry with electrochemical reaction followed by chemical reaction (EC mechanism) and CV with two following electrochemical reaction (EE mechanism). In update 1.1.0 has been added a general purpose CV function that allow to simulate up to 4 EE mechanism combined with chemical reaction for each species.Update 1.2.0 improved the accuracy of the measurements and allow personalized data resolution for simulation.
             Bibliography regarding this methods can be found in the following texts.
             Dieter Britz, Jorg Strutwolf (2016) <ISBN:978-3-319-30292-8>.
             Allen J. Bard, Larry R. Faulkner (2000) <ISBN:978-0-471-04372-0>.
	"""
	
	cran = "EleChemr" 

	version("1.2.0", md5="cd42bb00adb33e54393b9ead97370043")

	depends_on("r-ggplot2", type=("build", "run"))

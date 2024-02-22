# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhaser(RPackage):
	"""Phase Plane Analysis of One- And Two-Dimensional Autonomous ODE
Systems

	Performs a qualitative analysis of one- and two-dimensional
   autonomous ordinary differential equation systems, using phase plane methods.
   Programs are available to identify and classify equilibrium points, plot the
   direction field, and plot trajectories for multiple initial conditions. In
   the one-dimensional case, a program is also available to plot the phase
   portrait. Whilst in the two-dimensional case, programs are additionally
   available to plot nullclines and stable/unstable manifolds of saddle points.
   Many example systems are provided for the user. For further details can be
   found in Grayling (2014) <doi:10.32614/RJ-2014-023>.
	"""
	
	homepage = "https://github.com/mjg211/phaseR"
	cran = "phaseR" 

	version("2.2.1", md5="1a59537a0f040dee9c6f79df33b89f88")

	depends_on("r-desolve", type=("build", "run"))

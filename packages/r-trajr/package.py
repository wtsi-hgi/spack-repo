# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrajr(RPackage):
	"""Animal Trajectory Analysis

	A toolbox to assist with statistical analysis of animal trajectories.
    It provides simple access to algorithms for calculating and assessing a variety of 
    characteristics such as speed and acceleration, as well as multiple measures of 
    straightness or tortuosity. Some support is provided for 3-dimensional trajectories. 
    McLean & Skowron Volponi (2018) <doi:10.1111/eth.12739>. 
	"""
	
	homepage = "https://github.com/JimMcL/trajr"
	cran = "trajr" 

	version("1.5.1", md5="06400561f8c71f4b0cdc9bcc061c0e97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))

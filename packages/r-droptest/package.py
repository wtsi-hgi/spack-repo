# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDroptest(RPackage):
	"""Simulates LOX Drop Testing

	Generates simulated data representing the LOX drop testing
    process (also known as impact testing). A simulated process allows for
    accelerated study of test behavior. Functions are provided to simulate
    trials, test series, and groups of test series. Functions for creating plots
    specific to this process are also included. Test attributes and criteria can
    be set arbitrarily. This work is not endorsed by or affiliated with NASA.
    See "ASTM G86-17, Standard Test Method for Determining Ignition Sensitivity
    of Materials to Mechanical Impact in Ambient Liquid Oxygen and Pressurized
    Liquid and Gaseous Oxygen Environments" <doi:10.1520/G0086-17>.
	"""
	
	homepage = "https://github.com/chadr/droptest"
	cran = "droptest" 

	version("0.1.3", md5="b7e3cee39583352bc273c41924bc2723")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

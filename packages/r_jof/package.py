# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJof(RPackage):
	"""Modelling and Simulating Judgments of Frequency

	In a typical experiment for the intuitive judgment of frequencies (JoF) different stimuli with different frequencies are presented. The participants consider these stimuli with a constant duration and give a judgment of frequency. These judgments can be simulated by formal models: PASS 1 and PASS 2 based on Sedlmeier (2002, ISBN:978-0198508632), MINERVA 2 baesd on Hintzman (1984) <doi:10.3758/BF03202365> and TODAM 2 based on Murdock, Smith & Bai (2001) <doi:10.1006/jmps.2000.1339>. The package provides an assessment of the frequency by determining the core aspects of these four models (attention, decay, and presented frequency) that can be compared to empirical results.
	"""
	
	cran = "JoF" 

	version("0.1.0", md5="fa81b76e89fbaef7cae9f378d4e70c5e")

	depends_on("r@3.1:", type=("build", "run"))

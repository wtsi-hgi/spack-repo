# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsilicova(RPackage):
	"""Probabilistic Verbal Autopsy Coding with 'InSilicoVA' Algorithm

	Computes individual causes of death and population cause-specific mortality fractions using the 'InSilicoVA' algorithm from McCormick et al. (2016) <DOI:10.1080/01621459.2016.1152191>. It uses data derived from verbal autopsy (VA) interviews, in a format similar to the input of the widely used 'InterVA' method. This package provides general model fitting and customization for 'InSilicoVA' algorithm and basic graphical visualization of the output.
	"""
	
	homepage = "https://github.com/verbal-autopsy-software/InSilicoVA"
	cran = "InSilicoVA" 

	version("1.4.0", md5="b83525ad3dabb8ecfb98c97fb1ed155d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-interva5", type=("build", "run"))
	depends_on("java@1.7:", type=("build", "link", "run"))

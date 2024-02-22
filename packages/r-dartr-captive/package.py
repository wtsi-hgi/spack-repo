# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDartrCaptive(RPackage):
	"""Analysing 'SNP' Data to Support Captive Breeding

	Functions are provided that facilitate the analysis of SNP 
    (single nucleotide polymorphism) data to answer questions regarding 
    captive breeding and relatedness between individuals. 'dartR.captive' 
    is part of the 'dartRverse' suit of packages.
    Gruber et al. (2018) <doi:10.1111/1755-0998.12745>.
    Mijangos et al. (2022) <doi:10.1111/2041-210X.13918>.
	"""
	
	homepage = "https://green-striped-gecko.github.io/dartR/"
	cran = "dartR.captive" 

	version("0.75", md5="ae7a55982381b911ba71d5855f45a223")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
	depends_on("r-dartr-base", type=("build", "run"))
	depends_on("r-dartr-data", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

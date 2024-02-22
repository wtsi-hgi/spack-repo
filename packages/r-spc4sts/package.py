# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpc4sts(RPackage):
	"""Statistical Process Control for Stochastic Textured Surfaces

	Provides statistical process control tools for stochastic 
    textured surfaces. The current version supports the following tools:
    (1) generic modeling of stochastic textured surfaces.
    (2) local defect monitoring and diagnostics in stochastic 
        textured surfaces, which was proposed by Bui and Apley (2018a) 
        <doi:10.1080/00401706.2017.1302362>.
    (3) global change monitoring in the nature of stochastic 
        textured surfaces, which was proposed by Bui and Apley (2018b) 
        <doi:10.1080/00224065.2018.1507559>.
    (4) computation of dissimilarity matrix of stochastic textured 
        surface images, which was proposed by Bui and Apley (2019b)
        <doi:10.1016/j.csda.2019.01.019>.
	"""
	
	cran = "spc4sts" 

	version("0.6.3", md5="af296dac5ab32af1b0fcd2aeccbd2a7a")

	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))

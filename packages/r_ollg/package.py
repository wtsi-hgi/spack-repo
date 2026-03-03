# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROllg(RPackage):
	"""Computes some Measures of OLL-G Family of Distributions

	Computes the pdf, cdf, quantile function, hazard function and generating random numbers for Odd log-logistic family (OLL-G). This family have been developed by different authors in the recent years. See Alizadeh (2019) <doi:10.31801/cfsuasmas.542988> for example.
	"""
	
	homepage = "https://github.com/dmazarei/ollg"
	cran = "ollg" 

	version("1.0.0", md5="c67497faa25e8537e6026c4ea88cd0e4")


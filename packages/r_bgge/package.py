# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgge(RPackage):
	"""Bayesian Genomic Linear Models Applied to GE Genome Selection

	Application of genome prediction for a continuous variable, focused 
             on genotype by environment (GE) genomic selection models (GS). It consists a group of functions 
             that help to create regression kernels for some GE genomic models proposed by Jarquín et al. (2014) <doi:10.1007/s00122-013-2243-1>
             and Lopez-Cruz et al. (2015) <doi:10.1534/g3.114.016097>. Also, it computes genomic predictions based on Bayesian approaches.
             The prediction function uses an orthogonal transformation of the data and specific priors
             present by Cuevas et al. (2014) <doi:10.1534/g3.114.013094>.
	"""
	
	cran = "BGGE" 

	version("0.6.5", md5="01d0e7dd84918c09821a278360c4c0f9")

	depends_on("r@3.1.1:", type=("build", "run"))

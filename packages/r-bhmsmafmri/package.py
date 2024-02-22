# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhmsmafmri(RPackage):
	"""Bayesian Hierarchical Multi-Subject Multiscale Analysis of
Functional MRI (fMRI) Data

	Package BHMSMAfMRI performs Bayesian hierarchical multi-subject multiscale analysis of fMRI data as described in Sanyal & Ferreira (2012) <DOI:10.1016/j.neuroimage.2012.08.041>, or other multiscale data, using wavelet based prior that borrows strength across subjects and provides posterior smoothed images of the effect sizes and samples from the posterior distribution.
	"""
	
	homepage = "https://nilotpalsanyal.github.io/BHMSMAfMRI/"
	cran = "BHMSMAfMRI" 

	version("2.1", md5="e457eca9a169b137843e1f7a5b74a371")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

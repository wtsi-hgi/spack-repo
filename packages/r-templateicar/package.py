# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTemplateicar(RPackage):
	"""Estimate Brain Networks and Connectivity with ICA and Empirical
Priors

	Implements the template ICA (independent components analysis) model
    proposed in Mejia et al. (2020) <doi:10.1080/01621459.2019.1679638> and the 
    spatial template ICA model proposed in proposed in Mejia et al. (2022)
    <doi:10.1080/10618600.2022.2104289>. Both models estimate subject-level 
    brain as deviations from known population-level networks, which are 
    estimated using standard ICA algorithms. Both models employ an 
    expectation-maximization algorithm for estimation of the latent brain 
    networks and unknown model parameters. Includes direct support for 'CIFTI',
    'GIFTI', and 'NIFTI' neuroimaging file formats.
	"""
	
	homepage = "https://github.com/mandymejia/templateICAr"
	cran = "templateICAr" 

	version("0.6.4", md5="9670294b4b7626579bfb0395d1ed5160")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-excursions", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-fmritools@0.2.2:", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-pesel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

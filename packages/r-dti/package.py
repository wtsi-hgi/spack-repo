# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDti(RPackage):
	"""Analysis of Diffusion Weighted Imaging (DWI) Data

	Diffusion Weighted Imaging (DWI) is a Magnetic Resonance Imaging
             modality, that measures diffusion of water in tissues like the human
             brain. The package contains R-functions to process diffusion-weighted
             data. The functionality includes diffusion tensor imaging (DTI),
             diffusion kurtosis imaging (DKI), modeling for high angular resolution
             diffusion weighted imaging (HARDI) using Q-ball-reconstruction and
             tensor mixture models, several methods for structural adaptive
             smoothing including POAS and msPOAS, and a streamline fiber tracking
             for tensor and tensor mixture models.
             The package provides functionality to manipulate and visualize results
             in 2D and 3D.
	"""
	
	homepage = "https://www.wias-berlin.de/research/ats/imaging/"
	cran = "dti" 

	version("1.5.4", md5="97079f5db80885f51f269265960220e3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-awsmethods@1.1.1:", type=("build", "run"))
	depends_on("r-adimpro@0.9:", type=("build", "run"))
	depends_on("r-aws@2.4.1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-oro-nifti@0.3.9:", type=("build", "run"))
	depends_on("r-oro-dicom", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))

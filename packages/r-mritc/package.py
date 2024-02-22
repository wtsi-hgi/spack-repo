# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMritc(RPackage):
	"""MRI Tissue Classification

	Implements various methods for tissue classification in magnetic
        resonance (MR) images of the brain, including normal mixture models
        and hidden Markov normal mixture models, as outlined in Feng &
        Tierney (2011) <doi:10.18637/jss.v044.i07>. These methods allow a
        structural MR image to be classified into gray matter, white matter
        and cerebrospinal fluid tissue types.
	"""
	
	homepage = "https://github.com/jonclayden/mritc"
	cran = "mritc" 

	version("0.5-3", md5="0046fe91b39b3ae02f7965bac260276a")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lattice@0.18.8:", type=("build", "run"))
	depends_on("r-misc3d@0.8.1:", type=("build", "run"))
	depends_on("r-oro-nifti@0.4:", type=("build", "run"))

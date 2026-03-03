# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhitestripe(RPackage):
	"""White Matter Normalization for Magnetic Resonance Images

	Shinohara (2014) <doi:10.1016/j.nicl.2014.08.008>
    introduced 'WhiteStripe', an intensity-based normalization of T1 
    and T2 images, where normal 
    appearing white matter performs well, but requires segmentation.
    This method performs white matter mean and standard deviation
    estimates on data that has been rigidly-registered to the 'MNI'
    template and uses histogram-based methods.
	"""
	
	cran = "WhiteStripe" 

	version("2.4.2", md5="b99b362225c2f532b5f93f31c5fc99db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-oro-nifti@0.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-neurobase", type=("build", "run"))

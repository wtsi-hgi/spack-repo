# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmri(RPackage):
	"""Methods for Quantitative Magnetic Resonance Imaging ('qMRI')

	Implementation of methods for estimation of quantitative maps
    from Multi-Parameter Mapping (MPM) acquisitions (Weiskopf et al. (2013)
    <doi:10.3389/fnins.2013.00095>) including adaptive
    smoothing methods in the framework of the ESTATICS model
    (Estimating the apparent transverse relaxation time (R2*) from images with
    different contrasts, Weiskopf et al. (2014) <doi:10.3389/fnins.2014.00278>).
    The smoothing method is described in Mohammadi et al. (2017).
    <doi:10.20347/WIAS.PREPRINT.2432>. Usage of the package is also described in
    Polzehl and Tabelow (2019),
    Magnetic Resonance Brain Imaging, Chapter 6, Springer, Use R! Series.
    <doi:10.1007/978-3-030-29184-6_6>.
	"""
	
	homepage = "https://www.wias-berlin.de/research/ats/imaging/"
	cran = "qMRI" 

	version("1.2.7", md5="851bce5cf277e1b460950373ffdc043a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-awsmethods@1:", type=("build", "run"))
	depends_on("r-oro-nifti@0.9:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-aws@2.4:", type=("build", "run"))
	depends_on("r-adimpro@0.9:", type=("build", "run"))

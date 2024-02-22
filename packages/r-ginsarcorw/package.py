# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGinsarcorw(RPackage):
	"""GACOS InSAR Correction Workflow

	A workflow for correction of Differential Interferometric Synthetic Aperture Radar (DInSAR) atmospheric delay base on Generic Atmospheric Correction Online Service for InSAR (GACOS) data and correction algorithms proposed by Chen Yu. This package calculate the Both Zenith and LOS direction (User Depend). You have to just download GACOS product on your area and preprocessed D-InSAR unwrapped images. Cite those references and this package in your work, when using this framework.
    References: 
            Yu, C., N. T. Penna, and Z. Li (2017) <doi:10.1016/j.rse.2017.10.038>.
            Yu, C., Li, Z., & Penna, N. T. (2017) <doi:10.1016/j.rse.2017.10.038>.
            Yu, C., Penna, N. T., and Li, Z. (2017) <doi:10.1002/2016JD025753>.
	"""
	
	homepage = "<https://subhadipdatta.wixsite.com/profile/post/ginsarcorw-gacos-insar-correction-workflow>"
	cran = "GInSARCorW" 

	version("1.15.8", md5="dea1f8bf57d53d13bc357f5d7cbc179e")

	depends_on("r-raster", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))

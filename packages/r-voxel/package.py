# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoxel(RPackage):
	"""Mass-Univariate Voxelwise Analysis of Medical Imaging Data

	Functions for the mass-univariate voxelwise analysis of medical imaging data that follows the NIfTI <http://nifti.nimh.nih.gov> format. 
	"""
	
	homepage = "https://github.com/angelgar/voxel"
	cran = "voxel" 

	version("1.3.5", md5="a6d12b47ecf777a5f7ccae07a8aaadc1")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-lmertest@3.0.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gamm4", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))

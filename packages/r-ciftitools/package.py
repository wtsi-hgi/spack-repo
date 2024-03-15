# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiftitools(RPackage):
	"""Tools for Reading, Writing, Viewing and Manipulating CIFTI Files

	CIFTI files contain brain imaging data in "grayordinates," which 
    represent the gray matter as cortical surface vertices (left and right) and
    subcortical voxels (cerebellum, basal ganglia, and other deep gray matter). 
    'ciftiTools' provides a unified environment for reading, writing, 
    visualizing and manipulating CIFTI-format data. It supports the "dscalar," 
    "dlabel," and "dtseries" intents. Grayordinate data is read in as a "xifti" 
    object, which is structured for convenient access to the data and metadata,
    and includes support for surface geometry files to enable
    spatially-dependent functionality such as static or interactive 
    visualizations and smoothing.
	"""
	
	homepage = "https://github.com/mandymejia/ciftiTools"
	cran = "ciftiTools" 

	version("0.14.0", md5="bd0fbf6073135151103b4ae4b3625003")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-gifti@0.7.5:", type=("build", "run"))
	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))

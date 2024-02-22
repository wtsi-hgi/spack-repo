# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTractorBase(RPackage):
	"""Read, Manipulate and Visualise Magnetic Resonance Images

	Functions for working with magnetic resonance images. Reading and
    writing of popular file formats (DICOM, Analyze, NIfTI-1, NIfTI-2, MGH);
    interactive and non-interactive visualisation; flexible image manipulation;
    metadata and sparse image handling.
	"""
	
	homepage = "http://www.tractor-mri.org.uk"
	cran = "tractor.base" 

	version("3.3.5.1", md5="b19f48e7b25b568ca6c8b0bff9753482")

	depends_on("r-ore@1.3:", type=("build", "run"))
	depends_on("r-reportr", type=("build", "run"))
	depends_on("r-shades", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))

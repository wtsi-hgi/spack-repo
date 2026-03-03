# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROroNifti(RPackage):
	"""Rigorous - 'NIfTI' + 'ANALYZE' + 'AFNI' : Input / Output

	Functions for the input/output and visualization of
    medical imaging data that follow either the 'ANALYZE', 'NIfTI' or 'AFNI'
    formats.  This package is part of the Rigorous Analytics bundle.
	"""
	
	homepage = "https://rigorousanalytics.blogspot.com"
	cran = "oro.nifti" 

	version("0.11.4", md5="90d97d8a9bc898ccbb737d6da90135fe")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rnifti@0.9:", type=("build", "run"))

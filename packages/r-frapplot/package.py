# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrapplot(RPackage):
	"""Automatic Data Processing and Visualization for FRAP

	Automatically process Fluorescence Recovery After Photobleaching (FRAP) data and generate consistent, publishable figures. Note: this package does not replace 'ImageJ' (or its equivalence) in raw image quantification. Some references about the methods: Sprague, Brian L. (2004) <doi:10.1529/biophysj.103.026765>; Day, Charles A. (2012) <doi:10.1002/0471142956.cy0219s62>.
	"""
	
	homepage = "https://github.com/GuanqiaoDing/frapplot"
	cran = "frapplot" 

	version("0.1.3", md5="8d512f7102def829b734b0a4c2dd6b2e")

	depends_on("r@2.10:", type=("build", "run"))

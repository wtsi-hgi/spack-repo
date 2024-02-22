# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmzxmldata(RPackage):
	"""Reads Mass Spectrometry Data in mzXML Format

	Functions for reading mass spectrometry data in mzXML format.
	"""
	
	homepage = "https://strimmerlab.github.io/software/maldiquant/"
	cran = "readMzXmlData" 

	version("2.8.3", md5="1ffcbd4872c0591f1dd3814eb44e47b1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))

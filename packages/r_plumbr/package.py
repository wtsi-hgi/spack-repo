# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlumbr(RPackage):
	"""Mutable and Dynamic Data Models

	The base R data.frame, like any vector, is
    copied upon modification. This behavior is at odds with
    that of GUIs and interactive graphics. To rectify this,
    plumbr provides a mutable, dynamic tabular data model.
    Models may be chained together to form the complex
    plumbing necessary for sophisticated graphical
    interfaces. Also included is a
    general framework for linking datasets; an typical
    use case would be a linked brush.
	"""
	
	homepage = "https://github.com/ggobi/plumbr/wiki"
	cran = "plumbr" 

	version("0.6.10", md5="8d170a03736a4e207e01571648b6b7e4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-objectsignals@0.10.2:", type=("build", "run"))

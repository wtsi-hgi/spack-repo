# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2html(RPackage):
	"""HTML Exportation for R Objects

	Includes HTML function and methods to write in an HTML
        file. Thus, making HTML reports is easy. Includes a function
        that allows redirection on the fly, which appears to be very
        useful for teaching purpose, as the student can keep a copy of
        the produced output to keep all that he did during the course.
        Package comes with a vignette describing how to write HTML
        reports for statistical analysis. Finally, a driver for 'Sweave'
        allows to parse HTML flat files containing R code and to
        automatically write the corresponding outputs (tables and
        graphs).
	"""
	
	homepage = "https://github.com/nalimilan/R2HTML"
	cran = "R2HTML" 

	version("2.3.3", md5="0c5bf024dcf198df199aea7135f325dd")

	depends_on("r@2:", type=("build", "run"))

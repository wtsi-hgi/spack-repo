# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReplesentr(RPackage):
	"""Presentations in the REPL

	Create presentations and display them inside the R 'REPL'
    (Read-Eval-Print loop), aka the R console. Presentations can be written in
    'RMarkdown' or any other text format. A set of convenient navigation options
    as well as code evaluation during a presentation is provided. It is great
    for tech talks with live coding examples and tutorials. While this is not a
    replacement for standard presentation formats, it's old-school looks might
    just be what sets it apart. This project has been inspired by the
    'REPLesent' project for presentations in the 'Scala' 'REPL'.
	"""
	
	cran = "REPLesentR" 

	version("0.4.1", md5="54756aa75f8de28b0643e7a918642107")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-modules", type=("build", "run"))
	depends_on("r-dat", type=("build", "run"))
	depends_on("r-knitr@1.21.2:", type=("build", "run"))
	depends_on("pandoc@1.12:", type=("build", "link", "run"))

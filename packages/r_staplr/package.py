# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStaplr(RPackage):
	"""A Toolkit for PDF Files

	Provides functions to manipulate PDF files: 
    fill out PDF forms;
    merge multiple PDF files into one; 
    remove selected pages from a file;
    rename multiple files in a directory;
    rotate entire pdf document; 
    rotate selected pages of a pdf file;
    Select pages from a file;
    splits single input PDF document into individual pages;
    splits single input PDF document into parts from given points.
	"""
	
	cran = "staplr" 

	version("3.2.2", md5="4a6d4a0e3c974a9038c56fbafd24235f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))

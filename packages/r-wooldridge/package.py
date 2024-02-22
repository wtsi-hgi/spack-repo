# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWooldridge(RPackage):
	"""115 Data Sets from "Introductory Econometrics: A Modern
Approach, 7e" by Jeffrey M. Wooldridge

	Students learning both econometrics and R may find the introduction 
    to both challenging. The wooldridge data package aims to lighten the task by efficiently 
    loading any data set found in the text with a single command. Data sets have been 
    compressed to a fraction of their original size. Documentation files contain page numbers, 
    the original source, time of publication, and notes from the author suggesting avenues for 
    further analysis and research. If one needs an introduction to R model syntax, a 
    vignette contains solutions to examples from chapters of the text. 
    Data sets are from the 7th edition (Wooldridge 2020, ISBN-13 978-1-337-55886-0), 
    and are backwards compatible with all previous versions of the text.
	"""
	
	homepage = "https://justinmshea.github.io/wooldridge/"
	cran = "wooldridge" 

	version("1.4-3", md5="fc0cefbb19199b1d51226ee58113f5ad")

	depends_on("r@3.5:", type=("build", "run"))

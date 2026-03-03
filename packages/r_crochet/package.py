# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrochet(RPackage):
	"""Implementation Helper for '[' and '[<-' of Custom Matrix-Like
Types

	Functions to help implement the extraction / subsetting / indexing
    function '[' and replacement function '[<-' of custom matrix-like types
    (based on S3, S4, etc.), modeled as closely to the base matrix class as
    possible (with tests to prove it).
	"""
	
	homepage = "https://github.com/agrueneberg/crochet"
	cran = "crochet" 

	version("2.3.0", md5="e18ec54d3f5186fc3527bc547e98723b")

	depends_on("r@3:", type=("build", "run"))

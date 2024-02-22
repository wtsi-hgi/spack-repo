# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLaf(RPackage):
	"""Fast Access to Large ASCII Files

	Methods for fast access to large ASCII files.  Currently the
    following file formats are supported: comma separated format (CSV) and fixed
    width format. It is assumed that the files are too large to fit into memory,
    although the package can also be used to efficiently access files that do
    fit into memory. Methods are provided to access and process files blockwise.
    Furthermore, an opened file can be accessed as one would an ordinary
    data.frame. The LaF vignette gives an overview of the functionality
    provided.
	"""
	
	homepage = "https://github.com/djvanderlaan/LaF"
	cran = "LaF" 

	version("0.8.4", md5="e513183e9546ea3c0684dc990fe8c426")

	depends_on("r-rcpp", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBisdata(RPackage):
	"""Download Data from the Bank for International Settlements (BIS)

	Functions for downloading data from the Bank for
     International Settlements (BIS; <https://www.bis.org/>) in
     Basel.  Supported are only full datasets in (typically) CSV
     format.  The package is lightweight and without dependencies;
     suggested packages are used only if data is to be transformed
     into particular data structures, for instance into 'zoo'
     objects. Downloaded data can optionally be cached, to avoid
     repeated downloads of the same files.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/BISdata/"
	cran = "BISdata" 

	version("0.2-2", md5="92524c4b2ca545f3142d8a25c35d97af")


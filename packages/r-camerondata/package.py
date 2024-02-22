# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCamerondata(RPackage):
	"""Datasets from "Microeconometrics: Methods and Applications" by
Cameron and Trivedi

	Quick and easy access to datasets that let you replicate the
    empirical examples in Cameron and Trivedi (2005) "Microeconometrics: Methods and
    Applications" (ISBN: 9780521848053).The data are available as soon as you install
    and load the package (lazy-loading) as data frames. The documentation includes
    reference to chapter sections and page numbers where the datasets are used. 
	"""
	
	homepage = "https://github.com/juvlac/camerondata"
	cran = "camerondata" 

	version("1.0.0", md5="67426e840bf2379647f1d6000729394d")

	depends_on("r@3.5:", type=("build", "run"))

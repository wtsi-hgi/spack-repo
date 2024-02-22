# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedux(RPackage):
	"""R Bindings to 'hiredis'

	A 'hiredis' wrapper that includes support for
    transactions, pipelining, blocking subscription, serialisation of
    all keys and values, 'Redis' error handling with R errors.
    Includes an automatically generated 'R6' interface to the full
    'hiredis' API.  Generated functions are faithful to the
    'hiredis' documentation while attempting to match R's argument
    semantics.  Serialisation must be explicitly done by the user, but
    both binary and text-mode serialisation is supported.
	"""
	
	homepage = "https://github.com/richfitz/redux"
	cran = "redux" 

	version("1.1.4", md5="13eb2a35ff97ad02e09b1e42ec8cff7c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-storr@1.1.1:", type=("build", "run"))
	depends_on("hiredis", type=("build", "link", "run"))

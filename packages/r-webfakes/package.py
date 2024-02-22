# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebfakes(RPackage):
	"""Fake Web Apps for HTTP Testing

	Create a web app that makes it easier to test web clients
    without using the internet. It includes a web app framework with path
    matching, parameters and templates. Can parse various 'HTTP' request
    bodies. Can send 'JSON' data or files from the disk. Includes a web
    app that implements the 'httpbin.org' web service.
	"""
	
	homepage = "https://webfakes.r-lib.org/"
	cran = "webfakes" 

	version("1.3.0", md5="0d5a6f8dff6c26606b48f267063974a5")

	depends_on("r@3.6:", type=("build", "run"))

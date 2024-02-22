# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDomino(RPackage):
	"""R Console Bindings for the 'Domino Command-Line Client'

	A wrapper on top of the 'Domino Command-Line Client'. It lets you
    run 'Domino' commands (e.g., "run", "upload", "download") directly from your
    R environment. Under the hood, it uses R's system function to run the 'Domino'
    executable, which must be installed as a prerequisite. 'Domino' is a service
    that makes it easy to run your code on scalable hardware, with integrated
    version control and collaboration features designed for analytical workflows
    (see <http://www.dominodatalab.com> for more information).
	"""
	
	homepage = "http://www.dominodatalab.com"
	cran = "domino" 

	version("0.3.1", md5="ced8c8a280b96854254d180279632ffb")


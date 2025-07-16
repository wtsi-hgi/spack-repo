# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlaskServerTiming(PythonPackage):
	"""Python Flask Server-Timing Header Extension"""
	
	homepage = "https://github.com/rodrobin/flask-server-timing"
	pypi = "flask-server-timing/flask-server-timing-0.1.2.tar.gz" 

	version("0.1.1", sha256="71fbaff54803cbecb758e69a2b1b95cb84a118bd1e3208de410ecaa9f25d592f")
	version("0.1.2", sha256="e448683912089ada8d3af78c260687e1b5bfd0381430f8b52f7ff2a931166efa")

	depends_on("py-setuptools", type=("build"))

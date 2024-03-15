# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RPbdzmq(RPackage):
	"""Programming with Big Data -- Interface to 'ZeroMQ'.

	'ZeroMQ' is a well-known library for high-performance asynchronous
	messaging in scalable, distributed applications. This package provides high
	level R wrapper functions to easily utilize 'ZeroMQ'. We mainly focus on
	interactive client/server programming frameworks. For convenience, a
	minimal 'ZeroMQ' library (4.1.0 rc1) is shipped with 'pbdZMQ', which can be
	used if no system installation of 'ZeroMQ' is available. A few wrapper
	functions compatible with 'rzmq' are also provided."""

	cran = "pbdZMQ"

	license("GPL-3.0-or-later")

	version("0.3-11", md5="01d91cffe8b6ac672a1aa1c71ca76121")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("libzmq@4.0.7:", type=("build", "link", "run"))

# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYaml(RPackage):
	"""Methods to Convert R Data to YAML and Back.

	Implements the 'libyaml' 'YAML' 1.1 parser and emitter
	(<https://pyyaml.org/wiki/LibYAML>) for R."""

	cran = "yaml"

	license("BSD-3-Clause")

	version("2.3.8", md5="25606fd9de01159019b5acd8d0410af7")


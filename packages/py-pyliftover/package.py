# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyliftover(PythonPackage):
	"""Pure-python implementation of UCSC ``liftOver`` genome coordinate conversion."""
	
	homepage = "https://github.com/konstantint/pyliftover"
	pypi = "pyliftover/pyliftover-0.4.1-py3-none-any.whl" 

	version("0.1", sha256="49413709dc34f93e3f0d1e0ee459d2ade47acc61868ffee0365460c9c0286d37")
	version("0.2", sha256="3b23f8c7d31a57325e3fd5dbded762d748604116d4663e979b984b7991be6f3b")
	version("0.3", sha256="8feaa3106e55705291feb70bb82be0861d7ba2306911a3ad42ceed1a2df19299")
	version("0.4", sha256="72bcfb7de907569b0eb75e86c817840365297d63ba43a961da394187e399da41")
	version("0.4.1", sha256="49ef8938010d2e934abb483d3ef8073897ed6b88bcd978c486c8f7631c24dbc1", expand=False, url="https://files.pythonhosted.org/packages/b1/61/e3afcf369fe45223cfebfbb8cde46d521e2786889c1b3eed01ee08adb626/pyliftover-0.4.1-py3-none-any.whl")


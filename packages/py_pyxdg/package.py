# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyxdg(PythonPackage):
	"""PyXDG contains implementations of freedesktop.org standards in python."""
	
	homepage = "http://freedesktop.org/wiki/Software/pyxdg"
	pypi = "pyxdg/pyxdg-0.28-py2.py3-none-any.whl" 

	version("0.19", sha256="7a51fe373ba9e8a438efb5a605389b33c05d4e48d61ba401e1195fb88ff9ae19")
	version("0.20", sha256="7f405662bb5224eaa84812dee4d79e1210129c45b800b361070adb2e2b061199")
	version("0.21", sha256="85da4c37eedc2088035362ed7edd5d1c8fbd45d2bfecfe3f325fa85e6297f18b")
	version("0.22", sha256="e2580a45996c5e904dccb2b577b07a998757f567a41c8eb05e23e25028413e85")
	version("0.23", sha256="3bc1ecc85455f0fccceb95eaf998f6c56b483da59aa00d3beb5e095704866f4a")
	version("0.24", sha256="220487bcea2d67c8da2a21bb261d647e03519a0b1a631365e45c77632c9491b6")
	version("0.25", sha256="81e883e0b9517d624e8b0499eb267b82a815c0b7146d5269f364988ae031279d")
	version("0.26", sha256="1948ff8e2db02156c0cccd2529b43c0cff56ebaa71f5f021bbd755bc1419190e", expand=False, url="https://files.pythonhosted.org/packages/39/03/12eb9062f43adb94e30f366743cb5c83fd15fef026500cd4de42c7c12280/pyxdg-0.26-py2.py3-none-any.whl")
	version("0.27", sha256="2d6701ab7c74bbab8caa6a95e0a0a129b1643cf6c298bf7c569adec06d0709a0", expand=False, url="https://files.pythonhosted.org/packages/ea/13/de39ddf4f9f9cea0c7684cd54a50d79c97ea99c9f6aed798fd13d0bd4609/pyxdg-0.27-py2.py3-none-any.whl")
	version("0.28", sha256="bdaf595999a0178ecea4052b7f4195569c1ff4d344567bccdc12dfdf02d545ab", expand=False, url="https://files.pythonhosted.org/packages/e5/8d/cf41b66a8110670e3ad03dab9b759704eeed07fa96e90fdc0357b2ba70e2/pyxdg-0.28-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))

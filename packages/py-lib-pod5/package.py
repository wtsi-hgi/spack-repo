# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLibPod5(PythonPackage):
	"""Python bindings for the POD5 file format"""

	homepage = "https://github.com/nanoporetech/pod5-file-format"
	pypi = "lib-pod5/lib_pod5-0.3.28-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl"

	# Use a specific manylinux wheel with verified checksum
	version(
		"0.3.28",
		sha256="41a4c5a78ca58343e0d4b5daa493928d218fca14f663bb339658a26f2f1e5258",
		expand=False,
		url="https://files.pythonhosted.org/packages/5b/85/c41bf5696fa786756df4283796af6c757fef957173c84c98cdfa120caf4c/lib_pod5-0.3.28-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl",
	)

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:3.9", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))



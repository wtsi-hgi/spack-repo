# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBiofluff(PythonPackage):
	"""fluff : exploratory analysis and visualization of high-throughput sequencing data"""
	
	homepage = "https://github.com/simonvh/fluff/"
	pypi = "biofluff/biofluff-3.0.4.tar.gz" 

	version("2.0.1", sha256="c6d62eba31bdfed66eec67529dcb81d537f61d979e0ca9c5e29093063e533b7b")
	version("2.0.2", sha256="cd730662c9002ef2f80f00290417b6007289b123d8e144cd3b3c9db13d80b4f6")
	version("2.1.2", sha256="7a049b99fd4f4897ce710b16c68cc7070af2eda63a05c6b60b2ca19d31fe58e0")
	version("2.1.4", sha256="79fb9939c0ba3a6cbf65c4187ece1f0037e7d08551989aee12739da78c148991", expand=False, url="https://files.pythonhosted.org/packages/76/3f/6d46616e9e72c1eccecaed0d3d34240272bd5e7527aaa480550eae99c63e/biofluff-2.1.4-py2-none-any.whl")
	version("3.0.0", sha256="0da72aab3739d5be5f51edf9828a33a1d15f4470ca61f02a2e6f6e4a14d786cd")
	version("3.0.1", sha256="4de60a1188942cd9699f364680ba9495e8cf4d1378a4ae8679dc3519f4d606bf")
	version("3.0.2", sha256="63607f2d0117c6dd5cf9932580d6c2564d55eed4c05e9c4801902f25712ea03c")
	version("3.0.3", sha256="7f424f89b9b1a157e46b168b9d2b655dca2c8651e5e334bc807fcc0b728ff02b")
	version("3.0.4", sha256="ef7b0a54103a830f197f21aa3d1ade8bdcddf613b437ea38c95260bb45324d6b")

	depends_on("py-setuptools", type=("build"))

# {'HTSeq': ['2.1.4'], 'Pycluster': ['2.1.4'], 'colorbrewer': ['2.1.4'], 'matplotlib': ['2.1.4'], 'numpy': ['2.1.4'], 'pyBigWig': ['2.1.4'], 'pybedtools': ['2.1.4'], 'pysam': ['2.1.4'], 'scipy': ['2.1.4']}
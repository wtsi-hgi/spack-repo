# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVbzH5pyPlugin(PythonPackage):
	"""Oxford Nanopore Technologies VBZ HDF5 plugin loader for h5py."""

	homepage = "https://pypi.org/project/vbz-h5py-plugin/"
	pypi = "vbz_h5py_plugin/vbz_h5py_plugin-1.0.1-py3-none-any.whl"

	version("1.0.1", sha256="7b8f9bf250a3c072e36bb8a84beb035468bba0536e11a9086649188f075589b1", expand=False, url="https://files.pythonhosted.org/packages/d2/dd/eab7a9cac698afd8d4d469d703303390a88570ace01da358088459a6a48d/vbz_h5py_plugin-1.0.1-py3-none-any.whl")
	version("1.0.0", sha256="8bcdfd46a35dc8db9799fb990eeb12c0bfd90cb711c08133378ac704bec0562a", expand=False, url="https://files.pythonhosted.org/packages/e7/ad/7abbec7fe36afb118469f1c12e5603446c37fd0a3928412a950bda666931/vbz_h5py_plugin-1.0.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))
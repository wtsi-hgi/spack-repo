# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCellex(PythonPackage):
	"""Compute single-cell cell-type expression specificity"""
	
	homepage = "https://github.com/perslab/CELLEX"
	pypi = "cellex/cellex-1.2.2-py3-none-any.whl" 

	version("1.0.0", sha256="15144c6723ab6327d96a6f4f434eb6c4a9ea347ca7b8f032ba307b3ffab917ae", expand=False, url="https://files.pythonhosted.org/packages/b7/16/af3ed51a3d0be39211e9b72579023aa9f871e5338de073ea7698155904e2/cellex-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="f33913b89609a933d397f0ec3478b9d2db6fe8de37e758b45134de3e0e537a09", expand=False, url="https://files.pythonhosted.org/packages/a5/68/b3014c00f61edbd94a662dfabd306c1cdfcff845a7f4f99fd0f1bcc69266/cellex-1.1.0-py3-none-any.whl")
	version("1.1.1", sha256="b23d4805247078ef15d389069cf84f589c748fdab3b003199267668b26feecfc", expand=False, url="https://files.pythonhosted.org/packages/9b/ed/8a6023fa7c4436d544b5603ecffd33003d68b6de4e288a79bdbefe74a911/cellex-1.1.1-py3-none-any.whl")
	version("1.2.1", sha256="f505d61d843f6101ec50e2bbaec778c92ebf77f60b36e1dd23df49431fc3318f", expand=False, url="https://files.pythonhosted.org/packages/a6/7e/d3cbbf65bb5d0d19044e45c82183a19053cf76b3b2a88de08c52e13ffc4f/cellex-1.2.1-py3-none-any.whl")
	version("1.2.2", sha256="d3f7d920c038e547b07e25e524e64f14541178a5699b5da43f6cd76d253bf3da", expand=False, url="https://files.pythonhosted.org/packages/69/4b/1a4129468ef41d85eb00de019327e673083bd0159f1e632f0063003fa261/cellex-1.2.2-py3-none-any.whl")

	depends_on("py-plotnine", type=("build", "run"))
	depends_on("py-adjusttext", type=("build", "run"))
	depends_on("py-loompy", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy@:1.23", type=("build", "run"))
	depends_on("py-setuptools-scm", type=("build", "run"))
	depends_on("py-setuptools", type=("build", "run"))

# {'plotnine(==0.5.1)': ['1.0.0'], 'numpy(==1.17.0)': ['1.0.0'], 'scipy(==1.3.1)': ['1.0.0'], 'pandas(==0.25.0)': ['1.0.0'], 'setuptools(==41.0.1)': ['1.0.0'], 'h5py(==2.9.0)': ['1.0.0'], 'setuptools-scm(==3.3.3)': ['1.0.0'], 'setuptools(>=41.2.0)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'setuptools-scm(>=3.3.3)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'numpy(>=1.17.0)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'scipy(>=1.3.1)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'pandas(>=0.25.0)': ['1.1.0', '1.1.1'], 'h5py(>=2.9.0)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'loompy(>=3.0.6)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'adjustText(>=0.7.3)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'plotnine(>=0.6.0)': ['1.1.0', '1.1.1', '1.2.1', '1.2.2'], 'pandas(>=1.0.3)': ['1.2.1', '1.2.2']}
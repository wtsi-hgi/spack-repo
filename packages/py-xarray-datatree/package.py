# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyXarrayDatatree(PythonPackage):
	"""Hierarchical tree-like data structures for xarray"""
	
	homepage = "https://github.com/xarray-contrib/datatree"
	pypi = "xarray-datatree/xarray_datatree-0.0.9-py3-none-any.whl" 

	version("0.0.10", sha256="cfc762296915888e0020457b78f0b908514be67ac49d8cbb0ca571161c136a32", expand=False, url="https://files.pythonhosted.org/packages/da/99/2eaa47551d6408d65edd528c85994b35b9fe0fa880679066bc00ad60f53d/xarray_datatree-0.0.10-py3-none-any.whl")
	version("0.0.11", sha256="f839eb0738c85d20d8ee36595f0efd17a8dbe28bb5f093eb47059288b127b7a1", expand=False, url="https://files.pythonhosted.org/packages/db/4d/332a36b0239b472e2c6589e71df7b793910c9b340a328a98b9f163644837/xarray_datatree-0.0.11-py3-none-any.whl")
	version("0.0.12", sha256="6fef5356c7cca453308484e3a3fd9fab597542289dfcbf8b6b7e0262dfc4240d", expand=False, url="https://files.pythonhosted.org/packages/a6/72/d0b2bba98085d7a7e0226d73a4cbc474d1ac48c62d64d78bcab731178729/xarray_datatree-0.0.12-py3-none-any.whl")
	version("0.0.13", sha256="b5c92339339e58f029107fd3c50478adb1dfd1316eaa628d1e0e2e8a3e7a079a", expand=False, url="https://files.pythonhosted.org/packages/a5/ab/3f2b7a9a3543bf664c136159a3054767cb7ba1dc2c7ab7451a198e0aabb5/xarray_datatree-0.0.13-py3-none-any.whl")
	version("0.0.14", sha256="07f5d0d9a03a3220d732e1c764ee60f2c5110f884a290b2af371f92952379166", expand=False, url="https://files.pythonhosted.org/packages/6e/a3/5e92dc7e35c08574472bbd9201aabdad03e38d54cc47c421922d219502c6/xarray_datatree-0.0.14-py3-none-any.whl")
	version("0.0.15", sha256="190d8262061522eeaaa0dc7058b50df7228a615e6d62761150f093518bdad62c", expand=False, url="https://files.pythonhosted.org/packages/cb/e3/6952d37e19b66bd2f18a3de16289ad7da4ef649f6284e07942a5bf5931a8/xarray_datatree-0.0.15-py3-none-any.whl")
	version("0.0.2.post1", sha256="26735f0d8c89820c9357ae0202fd59c341a00d09241f1577ba6e3fafe3f15ebc", expand=False, url="https://files.pythonhosted.org/packages/32/3f/50dbaf25c76a4ee8fed9c67e5bf9bfff9cce8231b941c48cad8d79eff9e0/xarray_datatree-0.0.2.post1-py3-none-any.whl")
	version("0.0.3", sha256="946218aa6cd93f489943dbdd8a2eb7f8bf6bea8a83e7cea015ff0999837fa357", expand=False, url="https://files.pythonhosted.org/packages/1a/49/89a62e7f6c58f1abf2de8c71558ff49b7ddd3fe790561ddd8f0242abf766/xarray_datatree-0.0.3-py3-none-any.whl")
	version("0.0.4", sha256="d479b9521286f4b266583aee67c20f1a1a4121228573367ca20af08c2eaf947f", expand=False, url="https://files.pythonhosted.org/packages/e6/69/5cb8f3c5a4498aad55df52164ed0b278b33d6431b7301d3218647dced1c8/xarray_datatree-0.0.4-py3-none-any.whl")
	version("0.0.5", sha256="d9988352c760a370b167744a8ac68c558d163b0d1ce9404f7ad6f56f23464ee4", expand=False, url="https://files.pythonhosted.org/packages/d6/dc/04f8c02df1c9f8419a43af5e2cf31b73baba48e6e1d7957ca3df1fc98b71/xarray_datatree-0.0.5-py3-none-any.whl")
	version("0.0.6", sha256="6d1a92262650b18cb843932a7133127e517b60a45e2e48f9d2b88b4574d26a5d", expand=False, url="https://files.pythonhosted.org/packages/7d/db/8168bf51ea27fbf3235f18b6e7a7b0ca64046cd54cadee92e51b93569c96/xarray_datatree-0.0.6-py3-none-any.whl")
	version("0.0.9", sha256="3e9ca1e5ce0dce6ac84675ec836875beb24e450e0774659cbc8141311965db64", expand=False, url="https://files.pythonhosted.org/packages/cb/71/1dd70489753c4fe0a73d1a525669b85ddce26603bf3629ad9f6586c9b0a2/xarray_datatree-0.0.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-xarray", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))

# {'xarray(>=2022.6.0)': ['0.0.10', '0.0.11', '0.0.12'], 'xarray>=2022.6.0': ['0.0.13'], 'packaging': ['0.0.13', '0.0.14', '0.0.15'], 'xarray>=2023.12.0': ['0.0.14'], 'xarray<=2024.07.0,>=2023.12.0': ['0.0.15'], 'xarray(>=0.20.2)': ['0.0.2.post1', '0.0.3', '0.0.4', '0.0.5', '0.0.6'], 'anytree(>=2.8.0)': ['0.0.2.post1', '0.0.3', '0.0.4'], 'xarray(>=2022.05.0.dev0)': ['0.0.9']}
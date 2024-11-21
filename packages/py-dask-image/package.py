# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDaskImage(PythonPackage):
	"""Distributed image processing"""
	
	homepage = "https://image.dask.org"
	pypi = "dask-image/dask_image-2024.5.3-py3-none-any.whl" 

	version("0.1.0", sha256="83588955b0d0117fd9b667f5404aedccfaebfef7c83c1dc67cdc6b432b332a00")
	version("0.1.1", sha256="e6294ac577a8fc0abec2b97a2c42d404f599feac61d6899bdf1bf2b7cfb0e015")
	version("0.1.2", sha256="401e2c345a582eb2859a4a2a4a6fcfbc85beece59705f3ead9b6708a0cd183e7")
	version("0.2.0", sha256="bece2ea347f963dc0168c7d5fdfd11e51b47d9c857d3bc56144d7c146964a23f")
	version("0.3.0", sha256="603f9ddf59e4c69b8bdafcd5eadc99768160fb05cdcb78d14160c4533cf25b97")
	version("0.3.0rc1", sha256="7a0a1da285df53d76351b7e14aaf761693ba86137fcd1101e8ad17e2ae13460f")
	version("0.3.0rc3", sha256="4e31440ef1403ee7027a844aa06c6c3bf05b2c93cfef500d7972b80f3b3c8eab")
	version("0.4.0", sha256="a6873a39af21b856a4eb7efee6838e6897b1399f21ab9e65403e69eb62f96c2d")
	version("0.4.0rc1", sha256="a746960c998f03df5bcf6737c908b51f0b52ae30736c091bf68b383523add080")
	version("0.4.0rc2", sha256="88e51cfe15137424508cf949d09d2213cedb9870cfaaed603448a2d44476dbe2")
	version("0.5.0", sha256="0bf7ea8dcd9d795505b498bd632394720c048f50761e23c574d9a6bacfb27cbb")
	version("0.6.0", sha256="fee64c7fb5b2d2e27bdf250fea59bb5382496d94971c3bbf3ab68b52d7cefdff")
	version("0.6.0rc1", sha256="be2713e16cf629d970ec17532418143d2f9adc7681b85e40594813596532b2f0")
	version("2021.12.0", sha256="35be49626bd01c3e3892128126a27d5ee3266a198a8e3c7e30d59eaef712fcf9")
	version("2022.9.0", sha256="f123dfd16a7d15c76662a6ac14778509ed5eed9b494f4322e5945e9b15923547")
	version("2023.3.0", sha256="fa0ebff980c15dbc63d9b01a5ec551550a6dd637e6ae463f9de8ea2f9a2c851b", expand=False, url="https://files.pythonhosted.org/packages/5a/01/fae6fac53a725e068d4b9b09769a301d52d8a6827770fb8fdd45536f1338/dask_image-2023.3.0-py2.py3-none-any.whl")
	version("2023.3.0rc1", sha256="3d1c253ccfd649961149a2d3bd4a363e84abf190d38b7b75503008921c0d4d6f", expand=False, url="https://files.pythonhosted.org/packages/08/f5/481a13cede9921161555857440f586b9ca11a09e6d3f95adff89210f399d/dask_image-2023.3.0rc1-py2.py3-none-any.whl")
	version("2023.8.0rc2", sha256="39f35400dcb9fb63827e21ce84a88249a43d4c15bd76e7620803c3559625d323", expand=False, url="https://files.pythonhosted.org/packages/6f/35/d2bbed1f101ba4279238c74e8265b03072bd71e5b5e4138b0133832562cd/dask_image-2023.8.0rc2-py2.py3-none-any.whl")
	version("2023.8.1", sha256="15ef36a5fceedb2b2b3333f2cc18311cea840cc2aa2c4700999e07054a96266e", expand=False, url="https://files.pythonhosted.org/packages/0a/21/1191529271f917252a1f25a245aa81d8b207950937434b30d8eb3155b35e/dask_image-2023.8.1-py2.py3-none-any.whl")
	version("2024.5.0", sha256="820967ea72775ebfb742e54079575495d0a38d5b0142b1bad8820d1a44d09ff7", expand=False, url="https://files.pythonhosted.org/packages/9f/f7/a17dd9d74421a7fe747befe149d827d1497f1d7cbc52bfefaa5c5a479e0f/dask_image-2024.5.0-py3-none-any.whl")
	version("2024.5.0rc1", sha256="a86690105f51bd00a6f4772734a90f1d9364ce28da118f2b2911374f3d91f609", expand=False, url="https://files.pythonhosted.org/packages/19/df/1b7aed3b9d3fdfe48c70981263d3ea55842798ad0b3bcff630ec7a8ad27f/dask_image-2024.5.0rc1-py3-none-any.whl")
	version("2024.5.1", sha256="6c62b99480fc7ddffa9ac1c177f0db95e0d1677219f06964a6f5ba83e27b1327", expand=False, url="https://files.pythonhosted.org/packages/93/fc/e31b67b3b382e25619c797e643687c98e6c76a68c47a41ea1d5b17cfdfff/dask_image-2024.5.1-py3-none-any.whl")
	version("2024.5.2", sha256="1570b7bf9b729afca2b93d43849b05195a98521c37ba0838ce6a1464ac4a2bad", expand=False, url="https://files.pythonhosted.org/packages/39/45/517d4f7ee14665d6c1c8d887b86e5624bd4f61a137f3c9a1ad19e9bfcfe2/dask_image-2024.5.2-py3-none-any.whl")
	version("2024.5.3", sha256="b936f6d19a52974094cf8b7c6b51a3fdea77d9c7c80ca9862d764eda7ffbcd9a", expand=False, url="https://files.pythonhosted.org/packages/22/70/e34e5090865c3f840256c462e4671937270317fdf260871cd72546449d54/dask_image-2024.5.3-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-dask", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-pims", type=("build", "run"))
	depends_on("py-tifffile", type=("build", "run"))

# {'dask[array](>=2021.10.0)': ['2023.3.0', '2023.3.0rc1'], 'numpy(>=1.11.3)': ['2023.3.0', '2023.3.0rc1'], 'scipy(>=0.19.1)': ['2023.3.0', '2023.3.0rc1', '2023.8.0rc2', '2023.8.1'], 'pims(>=0.4.1)': ['2023.3.0', '2023.3.0rc1', '2023.8.0rc2', '2023.8.1'], 'tifffile(>=2018.10.18)': ['2023.3.0', '2023.3.0rc1', '2023.8.0rc2', '2023.8.1'], 'dask[array](>=2023.2.0)': ['2023.8.0rc2', '2023.8.1'], 'dask[dataframe](>=2023.2.0)': ['2023.8.0rc2', '2023.8.1'], 'numpy(>=1.18)': ['2023.8.0rc2', '2023.8.1'], 'pandas(>=2.0.0)': ['2023.8.0rc2', '2023.8.1'], 'dask[array,dataframe]>=2024.4.1': ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], 'numpy>=1.11.3': ['2024.5.0', '2024.5.0rc1'], 'scikit-image>=0.19.3': ['2024.5.0', '2024.5.0rc1'], 'scipy>=0.19.1': ['2024.5.0', '2024.5.0rc1'], 'pandas>=2.0.0': ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], 'pims>=0.4.1': ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], 'slicerator>=1.1.0': ['2024.5.0', '2024.5.0rc1'], 'tifffile>=2018.10.18': ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "cupy>=9.0.0;extra=='gpu'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "build>=1.2.1;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "coverage>=7.2.1;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "flake8>=6.0.0;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "Flake8-pyproject;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "pytest>=7.2.2;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "pytest-cov>=4.0.0;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "pytest-flake8>=1.1.1;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "pytest-timeout>=2.3.1;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], "twine>=3.1.1;extra=='test'": ['2024.5.0', '2024.5.0rc1', '2024.5.1', '2024.5.2', '2024.5.3'], 'numpy>=1.18': ['2024.5.1', '2024.5.2', '2024.5.3'], 'scipy>=1.7.0': ['2024.5.1', '2024.5.2', '2024.5.3']}
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNewick(PythonPackage):
	"""A python module to read and write the Newick format"""
	
	homepage = "https://gitlab.mpcdf.mpg.de/dlce-eva/python-newick"
	pypi = "newick/newick-1.9.0-py2.py3-none-any.whl" 

	version("0.1.0", sha256="57bac4444a8f13332c5b480d9c46f366da906b58b6de7742350c59289c4db6f7")
	version("0.2.0", sha256="7a197aac9d70f791de89382991a4dd567fd4405dfcc064b862506df571e24e1a")
	version("0.3.0", sha256="aaa0a75c49e940f1f21895551b92de8054ea7f05102b9bc17497d7aab0ee226d")
	version("0.4.0", sha256="3cf4b1b6d7391daeefb9263d0b1606559e4b2ac17444f737f8916a5241197eb5")
	version("0.5.0", sha256="b0dd7828062f1b88fc494c9e75bf9530eb6a504f570a673426b795bd60eaab62")
	version("0.6.0", sha256="cfbf232cd48f682cb75bf85acfce1a2d6c6153ca36a0876cd9896c907a9430cf")
	version("0.7.0", sha256="641c6764d7fb463e4fbe9da2ac6cec03b411be6758e0e5c547521b8e99a3865c")
	version("0.8.0", sha256="148371c1cce64093b3055e408f1b85576744ebc1085b9fa693e20f54d754b164")
	version("0.9.0", sha256="95fd041989815bc1813d0ca24098987c399c7fa63c588ec61e9c8f7477631202", expand=False, url="https://files.pythonhosted.org/packages/b6/91/47ed54f2dacdbb6743ede209a5d78c805debf017b4ea40f17f0243226812/newick-0.9.0-py2.py3-none-any.whl")
	version("0.9.1", sha256="ab120dbb5f6076a31a0019059b38935268ac01bb05239e3425bbf5f2f60a46a3", expand=False, url="https://files.pythonhosted.org/packages/36/79/fecac90c74d4dbbd47142d9f50469b7820060c37cf1e32243fe68e8fe7a6/newick-0.9.1-py2.py3-none-any.whl")
	version("0.9.2", sha256="92cd008bdb589e330ef704f68cbbef1039b508bd0e177e66d99ed048ad0d285a", expand=False, url="https://files.pythonhosted.org/packages/40/f0/3df31996857eb9798759a09dab9d01ada3ff1fc03e851bb456d8cdce2720/newick-0.9.2-py2.py3-none-any.whl")
	version("1.0.0", sha256="90dcaa3eb408dc54abb326f1b3ce1468da516fc7f4027518b8c085652a582d45", expand=False, url="https://files.pythonhosted.org/packages/95/1b/e47a990ef159820442b0b84752329a7a16c0ad08b0536c4872e8975bcfd4/newick-1.0.0-py2.py3-none-any.whl")
	version("1.1.0", sha256="0bb4712add4485114b243fca1f791428fcbc5aa5d71de74d3ef4f0d23e1b7437", expand=False, url="https://files.pythonhosted.org/packages/01/64/7b68f57c5418572d7029981c9b35015a62bda00f3562cf7c4692d9853c2b/newick-1.1.0-py2.py3-none-any.whl")
	version("1.10.0", sha256="898dc96a459517107ae38f8a500d5d1fcb42d4ae74bfddf13d1ba6a159bab626", expand=False, url="https://files.pythonhosted.org/packages/48/bb/274ce2f6672b2e37bd707bf2cc8f5e6ec8b037f0a95be212fe6ac882722a/newick-1.10.0-py2.py3-none-any.whl")
	version("1.2.0", sha256="06d7e3d9f51ae2b9f87af1b934c95d45bdf7389463213e20e4eea3980381169e", expand=False, url="https://files.pythonhosted.org/packages/d8/a6/3916dd398feab72a599baf872788d7913e2c212c0bd7e7c934e60e1ecaec/newick-1.2.0-py2.py3-none-any.whl")
	version("1.3.0", sha256="bad78cbabc055e8d8134c16116809bcefd91eb762662e298ebcfecdbce123f3f", expand=False, url="https://files.pythonhosted.org/packages/1b/e8/c1f667d1e2dcdba51079fd4cd022d1093f4e8f7f32c7b7cdaa474793fa93/newick-1.3.0-py2.py3-none-any.whl")
	version("1.3.1", sha256="ee044ec4d2587aaa79e12f0d7b73e41269c223815d8281f353e50ee5816c1cd2", expand=False, url="https://files.pythonhosted.org/packages/94/09/61e7611792965864f1e7f486db1bf54aa23df11b8935cded3a889d57a2fa/newick-1.3.1-py2.py3-none-any.whl")
	version("1.3.2", sha256="6fced6f48b045225ccc4ee4cdbfe78c42b538274f1b866c6add349cf02752fdd", expand=False, url="https://files.pythonhosted.org/packages/95/11/4db3f40c604b6cb1a574cbf06f66e217af03835385cca1605530d58cacc7/newick-1.3.2-py2.py3-none-any.whl")
	version("1.4.0", sha256="5a44d12b3cacab1a4450a1af483b1d9542e854bd326e461b30ad8f72415e15e4", expand=False, url="https://files.pythonhosted.org/packages/28/b5/8254e098b9f8d6dd2768451f26b38a0863a5410a319b16a7ace629c72f5e/newick-1.4.0-py2.py3-none-any.whl")
	version("1.5.0", sha256="a2f918ad1640729e5ecbc90d3d7f1506a33d7d63ffd42434c37c0a2f9e97d12a", expand=False, url="https://files.pythonhosted.org/packages/53/f5/a051dcce27695171f89722e465088689bef1dc3cc9d529de236cc41d58c1/newick-1.5.0-py2.py3-none-any.whl")
	version("1.6.0", sha256="60e1102acf8a4dd83393162e5f848ba2faced468d8a0165ce7614c259a8d4b5f", expand=False, url="https://files.pythonhosted.org/packages/db/1d/9ca295834da208442c2bc116a03162392f4e7a56f00f4a5cfd988a398a55/newick-1.6.0-py2.py3-none-any.whl")
	version("1.7.0", sha256="ba06725bf7ac4220823c52757c262684cd29616af3975d393cb135760baaea41", expand=False, url="https://files.pythonhosted.org/packages/b0/0d/60de977e66c8a718d6fca1a5c6b31a2942db59077fad4158a29aa2b2df7a/newick-1.7.0-py2.py3-none-any.whl")
	version("1.7.1", sha256="c5294771d9e9173642b8dcf5032b5be61c3a6e6ff83c4258ca587389e9c39f1f", expand=False, url="https://files.pythonhosted.org/packages/a1/da/baa599ce1672590abf09f504e2026b2b04033ecd2af33db2889dc62118e3/newick-1.7.1-py2.py3-none-any.whl")
	version("1.8.0", sha256="f481c0c5c78d71d5459d8aa47fc0e59242b7c8376ae87680a6835ddd69c5b043", expand=False, url="https://files.pythonhosted.org/packages/18/35/a33b2e5f9b4afbf6b3a07a0cb7e96fed65788400f5fe94a79fba622e8b72/newick-1.8.0-py2.py3-none-any.whl")
	version("1.8.1", sha256="eb7db47673fa8af794500f25c870d00c3c0410d8b5ca3d8fbdf029fa33e39b2f", expand=False, url="https://files.pythonhosted.org/packages/ba/e6/265b3e0a8e1f79336ff66be6fb8367509c476f71a490c823da3cf4fda741/newick-1.8.1-py2.py3-none-any.whl")
	version("1.9.0", sha256="25c262ca88a7752b5d759ff5bce7c85d50289ac2b06b13bb340e0a599c05bd02", expand=False, url="https://files.pythonhosted.org/packages/7d/32/2c71e873773a86abc2820fe3813372f9c53f6e5b8c1e42f69f2d82cd0221/newick-1.9.0-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.8:", type=("build", "run"))

# {"flake8;extra=='dev'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2', '1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "wheel;extra=='dev'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2'], "twine;extra=='dev'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2', '1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "pytest(>=3.1);extra=='test'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0'], "pytest-mock;extra=='test'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2', '1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "mock;extra=='test'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0'], "coverage(>=4.2);extra=='test'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2', '1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "pytest-cov;extra=='test'": ['0.9.0', '0.9.1', '0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2', '1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "ddt;extra=='test'": ['0.9.2', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.3.1'], "pytest(>=5);extra=='test'": ['1.1.0', '1.2.0', '1.3.0', '1.3.1', '1.3.2'], 'build;extra=="dev"': ['1.10.0'], 'tox;extra=="dev"': ['1.10.0'], 'flake8;extra=="dev"': ['1.10.0'], 'wheel>=0.36;extra=="dev"': ['1.10.0'], 'twine;extra=="dev"': ['1.10.0'], 'pytest>=3.6;extra=="test"': ['1.10.0'], 'pytest-mock;extra=="test"': ['1.10.0'], 'pytest-cov;extra=="test"': ['1.10.0'], 'coverage>=4.2;extra=="test"': ['1.10.0'], "build;extra=='dev'": ['1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "tox;extra=='dev'": ['1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "wheel(>=0.36);extra=='dev'": ['1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0'], "pytest(>=3.6);extra=='test'": ['1.4.0', '1.5.0', '1.6.0', '1.7.0', '1.7.1', '1.8.0', '1.8.1', '1.9.0']}
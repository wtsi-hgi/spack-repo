# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPycirclize(PythonPackage):
	"""Circular visualization in Python"""
	
	homepage = "https://moshi4.github.io/pyCirclize/"
	pypi = "pyCirclize/pycirclize-1.9.1-py3-none-any.whl" 

	version("0.0.1", sha256="294db16eb1bc89eccd4fb2d2b620e82e4c6d14e6dd7ac052d0c6a6178dc6e9af", expand=False, url="https://files.pythonhosted.org/packages/90/eb/de16bb03dd968d76d8c1e16b5a91b46340c5caf7d2dc846c23cec34e837b/pyCirclize-0.0.1-py3-none-any.whl")
	version("0.0.2", sha256="ed93a39c39fc56923373ec1e1f42e3d093f9b29373924be7690ad523f512f4db", expand=False, url="https://files.pythonhosted.org/packages/fc/f1/39b12d737e222f2c9ba0ad6dd13b03790ab3f3952433c8bf15ee918fe367/pyCirclize-0.0.2-py3-none-any.whl")
	version("0.0.3", sha256="2e8f154634edab3f37fd1fff90581b43df98a2298a9d56572b646907c7a7d88d", expand=False, url="https://files.pythonhosted.org/packages/7f/e1/af921e6dc9b3435c1e4716ec5e6381c05ed778b4b86db99f0f764e080131/pyCirclize-0.0.3-py3-none-any.whl")
	version("0.1.0", sha256="2d7f2cfcf964dfc5452e59a1c38e7af0e3f8a71f78675243b6c2c512d2e25955", expand=False, url="https://files.pythonhosted.org/packages/bb/05/2bb16906ca03f9b62c19b4943df7bc9287fe099c77f08d2f6d1ca7584322/pycirclize-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="e5fcaa6ffde7c7770c4b8d52c78f4364701c73628321291daab3ceefe32ecb0d", expand=False, url="https://files.pythonhosted.org/packages/ce/72/b9abe424c0453ea4290cb779e25580c24ca5e2750dc4c8d495185f145584/pycirclize-0.1.1-py3-none-any.whl")
	version("0.1.2", sha256="059befdacb5dcecfe13a59da55c459f4e379be25bd42cc54af64379a882c97ab", expand=False, url="https://files.pythonhosted.org/packages/f3/4b/47520512c2c28a20e8d553164310e00935e5ebaf3cdcc844fdc453e9a617/pycirclize-0.1.2-py3-none-any.whl")
	version("0.1.3", sha256="3bae1e873c87c4f57bd95f89cf20151d0d1ad2c725f2018ee9c1725da05589f5", expand=False, url="https://files.pythonhosted.org/packages/99/69/8afa707f0fefddb9a5414c68860e45a4268787f63982926f660b49790229/pycirclize-0.1.3-py3-none-any.whl")
	version("0.2.0", sha256="f1aaf75a2bbc63e2fe6f641aa4cc155e0817360b97ab7a3d1f004ab1841074d4", expand=False, url="https://files.pythonhosted.org/packages/b3/35/4706776ad49e9ffa945eeb97a8cdde469e6dbbe33a1373e51f4ba66616fc/pycirclize-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="216ff34f8714c2b15758d27d204613a0f9140f8ef486c63a92134de2441928b0", expand=False, url="https://files.pythonhosted.org/packages/db/32/a1779c61077c7145f75be10ea237faea906a821531f93ff9b4f8ee8c54f2/pycirclize-0.2.1-py3-none-any.whl")
	version("0.3.0", sha256="e71e1d4ef7922e6de29599aed3f3c2a2d3d44df1f567c8f6ba9ba4cc53817a12", expand=False, url="https://files.pythonhosted.org/packages/9f/a4/af59f4c033c271958ab42eb1297826a3952853e4710f18b140e5b478e403/pycirclize-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="7695d3b648b858b984691f215ccc135ad5c838e27fb28983bc7a4440ed2d8af2", expand=False, url="https://files.pythonhosted.org/packages/77/da/58749bc881b0afdb9beb63234047931d1397f2f3012e91b4f8880a5f8e56/pycirclize-0.3.1-py3-none-any.whl")
	version("0.4.0", sha256="e9b2d89493b94e261649a68e43b53cabf74c60cd1f0758fe3069efc594722288", expand=False, url="https://files.pythonhosted.org/packages/da/2f/ac25494e57cd56d1e7d585ab369478bbf428d359701d86d417254a960331/pycirclize-0.4.0-py3-none-any.whl")
	version("0.5.0", sha256="cd167b9112f5376a0a58d4f70f606aaca74cf17d4998c2bda60dbf0a0a1e59e3", expand=False, url="https://files.pythonhosted.org/packages/a6/97/e0bd5176b46deb8986b039e35ed943da1ffe338eeb1701a3db867a3db98c/pycirclize-0.5.0-py3-none-any.whl")
	version("0.5.1", sha256="8f49a888605d7628d048a757a1492a09b2a7c85552f157b70ae54967eb4fb28f", expand=False, url="https://files.pythonhosted.org/packages/0f/73/2bcd699dd75652b42607edbd056a1ba7557cf0ca88230c52614ef95bfed2/pycirclize-0.5.1-py3-none-any.whl")
	version("1.0.0", sha256="29697449aed9088c4ce3674049e8f0d8a4e25b210e30d73df10ede16cbac92bd", expand=False, url="https://files.pythonhosted.org/packages/87/6d/06d8d9d197131cdcf830f00a2a4836c350baaf80e4aca0845976dde116a3/pycirclize-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="d7d236e5af53488681fb819168a1db9f9f4f18734a8b4e2cdb1f172ab4b89a80", expand=False, url="https://files.pythonhosted.org/packages/d5/87/62c7474b6aa8ed2428b7c75e373339652ffdfae884957a308792dc3046d8/pycirclize-1.1.0-py3-none-any.whl")
	version("1.2.0", sha256="70123cff1d1ec658f6006e915f1f07847075928cca0d7f35a2d8115400709923", expand=False, url="https://files.pythonhosted.org/packages/32/e2/1032f51d49743272ac8cebbae64f0a7e452550cc3105983e2c287d86e1c3/pycirclize-1.2.0-py3-none-any.whl")
	version("1.3.0", sha256="7df84bd415c817c99958304e10b895166b157117479adc060d8ea8d4854ef148", expand=False, url="https://files.pythonhosted.org/packages/cc/ae/caabfb6944258b225eaedce05346125f946ab9569c24d83a8732ce76e9dc/pycirclize-1.3.0-py3-none-any.whl")
	version("1.4.0", sha256="0d49539440a0e1b08d586847df15011c95bb1b68a8fede7c31ef7b9f940134f6", expand=False, url="https://files.pythonhosted.org/packages/ec/83/89e0b29e9bea042775c78d945b94ed6f5f8d72a38f0dacd100073cee1561/pycirclize-1.4.0-py3-none-any.whl")
	version("1.5.0", sha256="c0c65789cbe06d2f763cbebef279ddf53bf57d23d873d24f197c3b1f25c9df88", expand=False, url="https://files.pythonhosted.org/packages/9e/c5/faa2bd35aa1ffb6f17916db3b5338add310b7844adb49a0d1337f60d07f7/pycirclize-1.5.0-py3-none-any.whl")
	version("1.6.0", sha256="edb7328cd7547cbc3ddc2b907d819b95644d33be7f9cdc890fc02c310f6a24ee", expand=False, url="https://files.pythonhosted.org/packages/53/88/5057388101794104ed45db72ac8abfa4c70bdd23e58ceb0f29bf8b492c27/pycirclize-1.6.0-py3-none-any.whl")
	version("1.7.0", sha256="d3fda3962dba6b8f759f385490dcc400e8ea52b8c0e0cfaf262de6525097590d", expand=False, url="https://files.pythonhosted.org/packages/ec/8d/8d0dedce291aef829f383c1d66e2360637e4bfc448a7218b91831d1f6d80/pycirclize-1.7.0-py3-none-any.whl")
	version("1.7.1", sha256="e0c049877b1ee47245866cc9968f2aded5fe3ead8a3333841536dc29fd14bc90", expand=False, url="https://files.pythonhosted.org/packages/97/60/d6e3e7428825350bc694abb9444ec7ec13b3f29860dace0c1f88cc79a8eb/pycirclize-1.7.1-py3-none-any.whl")
	version("1.7.2", sha256="331ee8857b0c21676166a0751facd4cbb3446d8b554e33a4f7464cba643204b8", expand=False, url="https://files.pythonhosted.org/packages/95/99/f8cb2ded862de13f0d1b54d37445564130b6a4d318b78c3c8beb1424577d/pycirclize-1.7.2-py3-none-any.whl")
	version("1.8.0", sha256="8df9bf216fe37dd7016792d8670d60b999b75a0d7fa728217c2d8e498181aba6", expand=False, url="https://files.pythonhosted.org/packages/d1/3d/e635d4747a00f45cc922882b9e3461e5abddfca466e087a259645425e96a/pycirclize-1.8.0-py3-none-any.whl")
	version("1.9.0", sha256="acf88849d8190bc50094eec502872d8642ff1d4892599c4822e6465f5e5c60e0", expand=False, url="https://files.pythonhosted.org/packages/16/0c/9bdce3c70bcfaa68cc386b875cf723b6bffede52efff388a51998a49d5d4/pycirclize-1.9.0-py3-none-any.whl")
	version("1.9.1", sha256="0d78f517cfaad7d958514dbb53cd999b9870a11ba2ea4eff6991616805307415", expand=False, url="https://files.pythonhosted.org/packages/d5/e9/7fa576d5d355f69bc014401659dc09e3fdef5ba42dda636b452788e44a52/pycirclize-1.9.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-biopython", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))

# {'biopython(>=1.79,<2.0)': ['0.0.1', '0.0.2', '0.0.3', '0.1.0', '0.1.1'], 'matplotlib(>=3.5.2,<4.0.0)': ['0.0.1', '0.0.2', '0.0.3', '0.1.0', '0.1.1'], 'numpy(>=1.21.1,<2.0.0)': ['0.0.1', '0.0.2', '0.0.3', '0.1.0', '0.1.1'], 'pandas(>=1.5.2,<2.0.0)': ['0.0.1'], 'pandas(>=1.3.5,<2.0.0)': ['0.0.2', '0.0.3', '0.1.0', '0.1.1'], 'biopython(>=1.79)': ['0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '1.0.0', '1.1.0', '1.2.0', '1.3.0'], 'matplotlib(>=3.5.2)': ['0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.4.0', '1.5.0', '1.6.0'], 'numpy(>=1.21.1)': ['0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.4.0', '1.5.0', '1.6.0'], 'pandas(>=1.3.5)': ['0.1.2', '0.1.3', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.0', '0.5.0', '0.5.1', '1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.4.0', '1.5.0', '1.6.0'], 'biopython(>=1.80)': ['1.4.0', '1.5.0', '1.6.0'], 'biopython>=1.80': ['1.7.0', '1.7.1', '1.7.2', '1.8.0', '1.9.0', '1.9.1'], 'matplotlib>=3.6.3': ['1.7.0', '1.7.1', '1.7.2', '1.8.0', '1.9.0', '1.9.1'], 'numpy>=1.21': ['1.7.0', '1.7.1', '1.7.2', '1.8.0', '1.9.0', '1.9.1'], 'pandas>=1.3.5': ['1.7.0', '1.7.1', '1.7.2', '1.8.0', '1.9.0', '1.9.1']}
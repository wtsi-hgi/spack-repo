# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyprojectApi(PythonPackage):
	"""API to interact with the python pyproject.toml based projects"""
	
	homepage = "https://pyproject-api.readthedocs.io"
	pypi = "pyproject-api/pyproject_api-1.9.1-py3-none-any.whl" 

	version("0.1.0", sha256="1f1afc464171b799b3622954105dd4ee01ea8b067a139520679cc168e44e9871", expand=False, url="https://files.pythonhosted.org/packages/04/4d/c88eca988a3dfe3cd8c677d6b7331f04b6a5cccac4fbc5a341add4e73703/pyproject_api-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="40fc604001e6a662f759f78b2132113eea5fa4731f96fdbf052719c104299371", expand=False, url="https://files.pythonhosted.org/packages/79/63/00137d8d4e303ab2827b0638f6999f9119699992a87f6cd9dfaedc1845e8/pyproject_api-0.1.1-py3-none-any.whl")
	version("1.0.0", sha256="4389c737433ac383c146a3795cbaa7a22553fc485b594722087af4c2472abe2c", expand=False, url="https://files.pythonhosted.org/packages/8f/10/29642f5e80a329d03495eaa8df7d602250a2bc36a52ac8a5d06aa87fb6a4/pyproject_api-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="6749d4de906c2f03a2e44a7b9451b714c8149d22fc0a84b121dbdcb0318e3902", expand=False, url="https://files.pythonhosted.org/packages/a4/1f/05640785dc68709482aff844a8410155c744001f3bbe2f84809f3bd6b56a/pyproject_api-1.1.0-py3-none-any.whl")
	version("1.1.1", sha256="d4e088384e993a0824cc0e207b14182c17ff59ab416419656422155243f59e05", expand=False, url="https://files.pythonhosted.org/packages/6e/b6/5f6ce5a0dcc86d9bd409a9ce6f0f4fd351686862487dae917702cce42372/pyproject_api-1.1.1-py3-none-any.whl")
	version("1.1.2", sha256="3a3e01e503e0951937b1004aa231d8dc289610624901695d334458d3526d654c", expand=False, url="https://files.pythonhosted.org/packages/92/96/8d281a92687c326a3ad424e5811b716af2f3ccff03d5aee0df964d5b2960/pyproject_api-1.1.2-py3-none-any.whl")
	version("1.10.0", sha256="8757c41a79c0f4ab71b99abed52b97ecf66bd20b04fa59da43b5840bac105a09", expand=False, url="https://files.pythonhosted.org/packages/54/cc/cecf97be298bee2b2a37dd360618c819a2a7fd95251d8e480c1f0eb88f3b/pyproject_api-1.10.0-py3-none-any.whl")
	version("1.10.1", sha256="fa9e6f66c35b5017e909825d8f2b5d5482ea699d7be809d21c03bd1f7317f36a", expand=False, url="https://files.pythonhosted.org/packages/79/d7/29e1e5e882f79133631f7bcace42d23db493f616463c157a1ab614bf69dd/pyproject_api-1.10.1-py3-none-any.whl")
	version("1.2.0", sha256="6b66f701585a67295673abab8aff472efc1aa452639f491c71f23cf1b635d1c8", expand=False, url="https://files.pythonhosted.org/packages/9c/0e/28c0b5e8f46c1373c8fa781b77bd0c0d60726e0ed9c1d2ea16503e6a0620/pyproject_api-1.2.0-py3-none-any.whl")
	version("1.2.1", sha256="155d5623453173b7b4e9379a3146ccef2d52335234eb2d03d6ba730e7dad179c", expand=False, url="https://files.pythonhosted.org/packages/ab/4d/a213bbb67791415ac51331e3549fa161b1540c92a275beaef5a4e59b0a90/pyproject_api-1.2.1-py3-none-any.whl")
	version("1.3.0", sha256="90d8ce5f7231dce7cdeedbda1568e3cd427ca0cb4cf56f3d936f61d7eca9cde0", expand=False, url="https://files.pythonhosted.org/packages/48/60/4f34c4beb1880c6d3c8d3aec4cc17c5403be8e546c50c9c220f4225eb1f9/pyproject_api-1.3.0-py3-none-any.whl")
	version("1.4.0", sha256="c34226297781efdd1ba4dfb74ce21076d9a8360e2125ea31803c1a02c76b2460", expand=False, url="https://files.pythonhosted.org/packages/5c/74/430827553d00b2a25294b651cd732b79659551485ae5968a439dd64f1d1e/pyproject_api-1.4.0-py3-none-any.whl")
	version("1.5.0", sha256="4c111277dfb96bcd562c6245428f27250b794bfe3e210b8714c4f893952f2c17", expand=False, url="https://files.pythonhosted.org/packages/25/8d/261289ccd17044fb1fdf99da1ece3fda631b61b53b3c49f02e21f3e8af00/pyproject_api-1.5.0-py3-none-any.whl")
	version("1.5.1", sha256="4698a3777c2e0f6b624f8a4599131e2a25376d90fe8d146d7ac74c67c6f97c43", expand=False, url="https://files.pythonhosted.org/packages/3e/39/5b1d0ac2c8fddd06b68edb38cf813e0659d940f7781ab38e8ade1e3387a1/pyproject_api-1.5.1-py3-none-any.whl")
	version("1.5.2", sha256="9cffcbfb64190f207444d7579d315f3278f2c04ba46d685fad93197b5326d348", expand=False, url="https://files.pythonhosted.org/packages/ce/a7/0666a457fe35518d998448a6606b5f66c4bf092864bac6ef7fc380da582b/pyproject_api-1.5.2-py3-none-any.whl")
	version("1.5.3", sha256="14cf09828670c7b08842249c1f28c8ee6581b872e893f81b62d5465bec41502f", expand=False, url="https://files.pythonhosted.org/packages/05/53/b225115e177eb54664ede5b68a23d6806d9890baa8ee66b8d87f0bdb6346/pyproject_api-1.5.3-py3-none-any.whl")
	version("1.5.4", sha256="ca462d457880340ceada078678a296ac500061cef77a040e1143004470ab0046", expand=False, url="https://files.pythonhosted.org/packages/69/50/b3c9acb6b46b70664cf4b278fc490e94333c19c1d429ee5220aaf2b0b3f6/pyproject_api-1.5.4-py3-none-any.whl")
	version("1.6.0", sha256="4d4c27dcef8de49a4705e5c5322d90775e0588650d134c7ad66d23ddb9c1fa53", expand=False, url="https://files.pythonhosted.org/packages/cf/88/46aabddea66a6ad622f557a6232d8d46b5b793fafe05da3667f9f3bc9f43/pyproject_api-1.6.0-py3-none-any.whl")
	version("1.6.1", sha256="4c0116d60476b0786c88692cf4e325a9814965e2469c5998b830bba16b183675", expand=False, url="https://files.pythonhosted.org/packages/cf/b4/39eea50542e50e93876ebc09c4349a9c9eee9f6b9c9d30f88c7dc5433db8/pyproject_api-1.6.1-py3-none-any.whl")
	version("1.7.0", sha256="03b3db63d0d72c63b9ebe5019b4474a87bcee6ed9811de9bf5eb7becdbe119c2", expand=False, url="https://files.pythonhosted.org/packages/5c/51/c9233a7771f6c5161016eb2af6e933372a5a5662af7b7240860681cf67f8/pyproject_api-1.7.0-py3-none-any.whl")
	version("1.7.1", sha256="2dc1654062c2b27733d8fd4cdda672b22fe8741ef1dde8e3a998a9547b071eeb", expand=False, url="https://files.pythonhosted.org/packages/de/88/c1451b66664ae596bae93928ff372f4da89c2c7250132ecb76cc99256c93/pyproject_api-1.7.1-py3-none-any.whl")
	version("1.7.2", sha256="17c025105f8d27e22ffe542fe7dff3391b3736191a28294773a1f3b9ed25282b", expand=False, url="https://files.pythonhosted.org/packages/8f/dc/aca55d46389e719182d48c9ec09ae7f7cc5f944bdf44f90e59984d8f78f5/pyproject_api-1.7.2-py3-none-any.whl")
	version("1.8.0", sha256="3d7d347a047afe796fd5d1885b1e391ba29be7169bd2f102fcd378f04273d228", expand=False, url="https://files.pythonhosted.org/packages/ba/f4/3c4ddfcc0c19c217c6de513842d286de8021af2f2ab79bbb86c00342d778/pyproject_api-1.8.0-py3-none-any.whl")
	version("1.9.0", sha256="326df9d68dea22d9d98b5243c46e3ca3161b07a1b9b18e213d1e24fd0e605766", expand=False, url="https://files.pythonhosted.org/packages/b0/1d/92b7c765df46f454889d9610292b0ccab15362be3119b9a624458455e8d5/pyproject_api-1.9.0-py3-none-any.whl")
	version("1.9.1", sha256="7d6238d92f8962773dd75b5f0c4a6a27cce092a14b623b811dba656f3b628948", expand=False, url="https://files.pythonhosted.org/packages/ef/e6/c293c06695d4a3ab0260ef124a74ebadba5f4c511ce3a4259e976902c00b/pyproject_api-1.9.1-py3-none-any.whl")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySelfies(PythonPackage):
	"""SELFIES (SELF-referencIng Embedded Strings) is a general-purpose, sequence-based, robust representation of semantically constrained graphs."""
	
	homepage = "https://github.com/aspuru-guzik-group/selfies"
	pypi = "selfies/selfies-2.1.2-py3-none-any.whl" 

	version("0.1.1", sha256="4cb93a32c822e29ce82f1432b5ae23c817b38562836f8a7d95a70d9c148f595a", expand=False, url="https://files.pythonhosted.org/packages/07/08/8b391bbb0bf7944080460495ade83b326f1b7e2d28b96051d149b90cb572/selfies-0.1.1-py3-none-any.whl")
	version("0.2.0", sha256="153ca7bcff9c4525d93520d42505a5d4e44b682b5951907ff259f6e64861af85", expand=False, url="https://files.pythonhosted.org/packages/1c/50/2cd49bee6d75451ee48b611db5b1009faf66ad24af33572e8f6dc2e8f61c/selfies-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="946746cc24ff434793ff5f5231eb2468aeb195ea3df5a89a6571b9995bf1cabf", expand=False, url="https://files.pythonhosted.org/packages/8a/04/1d10f76ee389d2616600d10e91d9bb18176d7cf14e1f13836a4f125d99eb/selfies-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="367820d404f462705555747e6b5fb39b258106296e1084451447fb3d8fc60fb5", expand=False, url="https://files.pythonhosted.org/packages/85/64/161bcab8e81aa4f30dfa64e611741810fd5acd58efabb0ffb947c7f9b80a/selfies-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="e44c856d4fc9952121ed6512d0d9f8f1087b614a98861ea58ee3960d1b0d74cf", expand=False, url="https://files.pythonhosted.org/packages/08/b2/084baebea4b33b44026b2ccc451557095e6f4e907acaec01001195a414eb/selfies-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="b23692fec36d3b3149d109452b108a4e5dab6744013447051ff0453a8a032a79", expand=False, url="https://files.pythonhosted.org/packages/01/67/f8f04deb5bc03b0ff8c7c994802620e62257373c56169485c7465c82235e/selfies-0.2.4-py3-none-any.whl")
	version("1.0.0", sha256="0dfd260577b7a712d7e0eae03bd7e4fc8ca4d188f9b42d2824cf9310f4a837cc", expand=False, url="https://files.pythonhosted.org/packages/58/a9/afd485f76bc06a77d866b2b5442ef06eb5fe59fa6c309159988064115010/selfies-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="dc64cc89502a3908cec8df3107b053cc4f6a4f39db975df6a9091f487c2d82e8", expand=False, url="https://files.pythonhosted.org/packages/b1/cc/46ed417d9692cd598f9d5fd68cceaa2807a3fdcc50162eabee2dbbb55f6d/selfies-1.0.1-py3-none-any.whl")
	version("1.0.2", sha256="ccbf659bc6cfd04adb04f3b8cb0d9f9771f37ba7449082e9d07ef0ae5aabf403", expand=False, url="https://files.pythonhosted.org/packages/58/1b/d82fe9ea4c7713c5270205d6a434ad9c470bf1e906b4e260069dcaf9170a/selfies-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="4ceb3fdd36d587890a80156bb1f52128f0353443768811e5f7f9bb7506ee37cc", expand=False, url="https://files.pythonhosted.org/packages/cc/a5/4b190ee192394068827f06a9e391f3e169cf6265b6491ef8a654cb763dcb/selfies-1.0.3-py3-none-any.whl")
	version("1.0.4", sha256="e41009c1b5512d87ed8ea4d2a52ea9d833fbe6ddeb9ea34990b4a4d77b5b037c", expand=False, url="https://files.pythonhosted.org/packages/ad/d8/9ee274ee002188a3e343df1575fde1d5e6a270dcb98560a65928b4abb5d3/selfies-1.0.4-py3-none-any.whl")
	version("2.0.0", sha256="3cbe354dfb3ff7b506f493de2318930e4d627a664da902df47659fbba7ab3376", expand=False, url="https://files.pythonhosted.org/packages/f5/25/463b12b9b048dd805c25636e982895a259bf3e3411f16ca85de4da8f89a0/selfies-2.0.0-py3-none-any.whl")
	version("2.1.0", sha256="26021983fa8f70b587ec9564a4b5040a137ee09e168733c6ea679413b3567d1e", expand=False, url="https://files.pythonhosted.org/packages/4a/b2/953aa795375f5dd667099cb69488904bfb7125186c48d3b134bde81367a2/selfies-2.1.0-py3-none-any.whl")
	version("2.1.1", sha256="5723d53cd75e8229ff4ecef5a7872ce5151ad2ef83a0898b529ee5666a91621b", expand=False, url="https://files.pythonhosted.org/packages/a6/0a/85449549d49196280bb20067261634ecd4c9eafb326b4d627cf97b26fba9/selfies-2.1.1-py3-none-any.whl")
	version("2.1.2", sha256="30f675b9b0e9ac71d8489b36cc19e82389dbf319260743d90c9de5d19587b98f", expand=False, url="https://files.pythonhosted.org/packages/5c/ea/ddf401b64a42bebb28bf83319740725e4de418760bb4a23757e9f89393a6/selfies-2.1.2-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaex(PythonPackage):
    """Out-of-Core DataFrames to visualize and explore big tabular datasets"""

    homepage = "https://www.github.com/vaexio/vaex"
    pypi = "vaex/vaex-4.9.2-py3-none-any.whl"

    version(
        "4.0.1",
        sha256="db200580bf1cb869e7ccd52ea67b755754da813a4efc584379c3c8a984cd3421",
        expand=False,
        url="https://files.pythonhosted.org/packages/9f/9c/b8e3d0a8dbf5d11d7c06412dcca6fa9a54e4c8f93daffe3c1b494727e89d/vaex-4.0.1-py3-none-any.whl",
    )
    version(
        "4.1.0",
        sha256="a0d7148596b1302d488229c9e3a9481c2d056cc5042e0efb72739fad6c7e0b78",
        expand=False,
        url="https://files.pythonhosted.org/packages/61/1d/a5944560e4a86a6abb6906fa7a19f285b5a2e901b65b1891b9b573295616/vaex-4.1.0-py3-none-any.whl",
    )
    version(
        "4.11.0",
        sha256="dddbd30573a268b70a0b7796e2a83af17d7bea716e713e8fdc095156f4902032",
        expand=False,
        url="https://files.pythonhosted.org/packages/92/c7/af0d04194b59f2b7af113a8707e225b1b2dff560d653f354894f900d468e/vaex-4.11.0-py3-none-any.whl",
    )
    version(
        "4.11.1",
        sha256="b7dce849360a65e4e735faecd907079f4f206579982a9db919a1bf0f448b5bf4",
        expand=False,
        url="https://files.pythonhosted.org/packages/4d/00/c00874ec9a75b361420b6247610fdb1a9eae098c280237ceed8ae5013d55/vaex-4.11.1-py3-none-any.whl",
    )
    version(
        "4.12.0",
        sha256="e89fd4187cf72c039473ea2a6dc9a9ddfbb3b1c8f00c798aa64a5a3f711e41b6",
        expand=False,
        url="https://files.pythonhosted.org/packages/ba/84/92efc367605c1caa74c8debcac9d13b1a188715183def722db37b9721c97/vaex-4.12.0-py3-none-any.whl",
    )
    version(
        "4.13.0",
        sha256="7f3e3318e41fd7bbc9e943ef50237bb264c292d4579eac448c7952b495eb1cde",
        expand=False,
        url="https://files.pythonhosted.org/packages/ed/ca/c4ca78f742b02f77c583e91f3cf6fda0e5dd97337295f27f8305c5531417/vaex-4.13.0-py3-none-any.whl",
    )
    version(
        "4.14.0",
        sha256="c43be5c8baf327608db91907fead0080c3ddee75f1339102b439499fd410026f",
        expand=False,
        url="https://files.pythonhosted.org/packages/9b/10/5f1747fd759ec2c1dc60e83346726e196499c343603f7005bda8b48bdb00/vaex-4.14.0-py3-none-any.whl",
    )
    version(
        "4.15.0",
        sha256="6a016f56a2984e564d5f590ee721dddb2f2ab91161519f15d5e16e01cf470510",
        expand=False,
        url="https://files.pythonhosted.org/packages/4b/d8/f1e949a97f5682e883ecee98749a54bc1c10df026dd30ecd0ddd269c6a57/vaex-4.15.0-py3-none-any.whl",
    )
    version(
        "4.16.0",
        sha256="e2a03b2c391c8bbbc3d56098f241307fcdbdbd508599442939a8a58127ff14a4",
        expand=False,
        url="https://files.pythonhosted.org/packages/94/fa/8b319f3cef8adb9a9d02b44f3b6c6055f51c0560f70101152decefce9b2e/vaex-4.16.0-py3-none-any.whl",
    )
    version(
        "4.17.0",
        sha256="b48dafa590028b103d7a21dcf31d0ea511d83714899a97644eca96f3725bf7cc",
        expand=False,
        url="https://files.pythonhosted.org/packages/17/4d/e42547bc4d263bd15fb3c097f3f5510ec4752766d4ee32d80db58898f70b/vaex-4.17.0-py3-none-any.whl",
    )
    version(
        "4.2.0",
        sha256="0a0053a6e941e9a20d274ba4c44a28ec4cd8a46b5b602cd3909fd18ecd5a3476",
        expand=False,
        url="https://files.pythonhosted.org/packages/f8/0b/a248e6f7d7b88cc0d58087867812c487c6711ca893212b833ca000731fa6/vaex-4.2.0-py3-none-any.whl",
    )
    version(
        "4.3.0",
        sha256="ab2b6e65dee6297487d3c285e1e446b3a8544dc32880a94ce398cd07d948e0c2",
        expand=False,
        url="https://files.pythonhosted.org/packages/ea/fd/1ecdff00708560a714157fd7039a16bcd7e3718796c733f56f19bb47350d/vaex-4.3.0-py3-none-any.whl",
    )
    version(
        "4.4.0",
        sha256="68b78cca0829f00e200aa449d820166ab5be815ba7c275140b140546c57d6af7",
        expand=False,
        url="https://files.pythonhosted.org/packages/7f/d5/36ed35478dea8429b6c53ef16e370958543aa4b7a0f63a99b0f51a75213d/vaex-4.4.0-py3-none-any.whl",
    )
    version(
        "4.5.0",
        sha256="1886e047aa34939f0efe8e4807cd867911c9f751f47c70b36f8bd8f70f697ed9",
        expand=False,
        url="https://files.pythonhosted.org/packages/66/a1/12c8dc1298321c209984207acd2704025d4416ababda8b4d6240ca2605e1/vaex-4.5.0-py3-none-any.whl",
    )
    version(
        "4.6.0",
        sha256="d635fd40bb54d0d76c51d1pfff1b288187920490bd60e951a8e5cff35995b6c9c",
        expand=False,
        url="https://files.pythonhosted.org/packages/21/72/2548fac9e1245cc52be644d21c9e006e3c8ed686d525814ceaffde9dca30/vaex-4.6.0-py3-none-any.whl",
    )
    version(
        "4.7.0",
        sha256="9713ca0915f9e744e381fbcb42d242df00fc8edf51391ea5a2d60c0c692c59f4",
        expand=False,
        url="https://files.pythonhosted.org/packages/bb/05/6b25c979353372b013fbe4b03ab128f35971135b1897bb354202ba9f4f8c/vaex-4.7.0-py3-none-any.whl",
    )
    version(
        "4.8.0",
        sha256="18ca80302f1935700d77706421423a952ee94894bc30b1bde015b334d85d5d33",
        expand=False,
        url="https://files.pythonhosted.org/packages/e8/05/be2918e728b1c5b6be83360d06163b39e47327125cf3b2a79a2e86d4cd3f/vaex-4.8.0-py3-none-any.whl",
    )
    version(
        "4.9.0",
        sha256="4dd1da30aad8f982e04d6f6a6dfca2b0e3e0ff01f6b26918e17d87e0c0b2c6a1",
        expand=False,
        url="https://files.pythonhosted.org/packages/f5/63/4cdf2bfd9c894378a82bd5d5c7b9374e5e53aa17a5e70519e5fbd32adc64/vaex-4.9.0-py3-none-any.whl",
    )
    version(
        "4.9.1",
        sha256="1e4013da5598f5c01ae164466a951c0658dba2b7daf44b6bd89e095619f83724",
        expand=False,
        url="https://files.pythonhosted.org/packages/c7/a4/d5d5be2ca7dfb7cfa507b4bf59ec1f5b4594ba0f47dcfa1679a4fcd66cfa/vaex-4.9.1-py3-none-any.whl",
    )
    version(
        "4.9.2",
        sha256="32a16476abe7b4b27f30cba9f93e5720ed0e6938b476fedb4871f9fbdf500e78",
        expand=False,
        url="https://files.pythonhosted.org/packages/93/7c/ceab53e1639332b8590dc20c3ac1eaa203ccb7739bdf9e6f8afc9e91d21d/vaex-4.9.2-py3-none-any.whl",
    )

    depends_on("py-vaex-ml", type=("build", "run"))
    depends_on("py-vaex-jupyter", type=("build", "run"))
    depends_on("py-vaex-server", type=("build", "run"))
    depends_on("py-vaex-viz", type=("build", "run"))
    depends_on("py-vaex-hdf5", type=("build", "run"))
    depends_on("py-vaex-astro", type=("build", "run"))

    with default_args(type=("build", "link", "run")):
        depends_on("py-vaex-core@4.0.1", when="@4.0.1")
        depends_on("py-vaex-core@4.1.0", when="@4.1.0")
        depends_on("py-vaex-core@4.11.0", when="@4.11.0")
        depends_on("py-vaex-core@4.11.1", when="@4.11.1")
        depends_on("py-vaex-core@4.12.0", when="@4.12.0")
        depends_on("py-vaex-core@4.13.0", when="@4.13.0")
        depends_on("py-vaex-core@4.14.0", when="@4.14.0")
        depends_on("py-vaex-core@4.15.0", when="@4.15.0")
        depends_on("py-vaex-core@4.16.0", when="@4.16.0")
        depends_on("py-vaex-core@4.17.0", when="@4.17.0")
        depends_on("py-vaex-core@4.2.0", when="@4.2.0")
        depends_on("py-vaex-core@4.3.0", when="@4.3.0")
        depends_on("py-vaex-core@4.4.0", when="@4.4.0")
        depends_on("py-vaex-core@4.5.0", when="@4.5.0")
        depends_on("py-vaex-core@4.6.0", when="@4.6.0")
        depends_on("py-vaex-core@4.7.0", when="@4.7.0")
        depends_on("py-vaex-core@4.8.0", when="@4.8.0")
        depends_on("py-vaex-core@4.9.0", when="@4.9.0")
        depends_on("py-vaex-core@4.9.1", when="@4.9.1")

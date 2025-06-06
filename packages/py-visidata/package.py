# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVisidata(PythonPackage):
    """terminal interface for exploring and arranging tabular data"""

    homepage = "https://visidata.org"
    pypi = "visidata/visidata-3.1.1-py3-none-any.whl"

    version("0.37", sha256="713c6b357326030e960e67028dd4dd0e06b43c9f589dc474877643d14e01a752")
    version("0.41", sha256="2480ef5e312a06ecf5a8890961680b192b7e838d8244d34502a5f9d5a5ee0752")
    version("0.41.1", sha256="6c27c0489f3c1a5e88a707044d8fea6f5135dcb9d1d70f724654f6987b863fc9")
    version("0.59", sha256="9695c8ecd0f77dcf6f9851edda730f89aae9998a6f51f521c576f67d2f6089f9")
    version("0.60", sha256="0ee1e7071a6d6782116d5645f2e3dc5274cf48aaf0e7fb33b2ac13d57e90ad31")
    version("0.61", sha256="7073493b676564b21386b4c8f378cd81145873fe80b5c5b8a80ef0a8e2e5134b")
    version("0.80", sha256="4b92d8479cbf1cfdf5a7861e9df2cbc41ce490f91e287ae9f8152988b961dcf6")
    version("0.9", sha256="0d867db6ce49235f2e7a4529baac091819a97e263f1829a80c87642c12de051d")
    version("0.90", sha256="6e0e512775eff3aa665817d4b0f2ff47a80d01d6ee832c7f0d3b470107e5349b")
    version("0.91", sha256="6e26bf724863c4fb1a2cccb7b4b5849f4f36600b987f92aa5d62790d2d9c7632")
    version("0.92", sha256="910e8abdcb4f67d26f15324028ef4471234eecdae206cef414ef47c69ee79870")
    version("0.93", sha256="a4ee322fd22499b372a143992c9fa4de7ee9f71a858c27d1cc66515c50619283")
    version("0.94", sha256="0d0d6f6d3f3594962782b7db435eecaad896b9cf6279b0a0607b06b05138daaa")
    version("0.95.2", sha256="b499bb01adec06e2dc18eff493999cf0ed2235e9cb27a8d70c60d68cdc4b2ceb")
    version("0.96", sha256="c44b2f972ac1f8be74af7a9ccd529d7955b21f0849b125ae826783e587ab227a")
    version("0.97", sha256="64bf9c6992c1dd6db9540c94cbea054bc1b31bf894a59287f7723695d8a61f34")
    version("0.97.1", sha256="7cd48ad4208d3546bfb70f4f81490e91f9ac87d8f313095c1ce51ce0dc537c66")
    version("0.98", sha256="dbc92ee1f27e092fa22d354e0f36790d3932a09253625255ce74579de10af1fd")
    version("0.98.1", sha256="98b5a859d6de161b919a940bed0db5181a1fe63ea4d9151fc5374cd0c04ca713")
    version("0.99", sha256="52677c5886d6e769e34aeb6ffb75ad18ce633ac3bf005b8c7d99e8cd1474330e")
    version("1.0", sha256="79ad431f6bc1c4df7f8ecd8b26421d03f49f186c4e883b73310ffc5747b5a653")
    version("1.1", sha256="ae8b62f78ca30fc14695813694fea1d8b571b4a45efd61ced1ce1681e8edf36e")
    version("1.2", sha256="042efc2c43edaf3c3f8bd1bbf3c5d515663db66c41e81eea5f8b09200c2744e1")
    version("1.2.1", sha256="1b10e860ee4dcc738087fe215bfe7d9fad6f5b9eaea90cff44f7d71573b1def7")
    version("1.3", sha256="f087a3c990527885675934767b0ad893db65e83b832b2eeb51aba2e11d6c7f35")
    version("1.3.1", sha256="2b2fc55c6c25d2d0b60687a898fe78c6590df822e4927252d6b093085b3e7bea")
    version("1.4", sha256="86c78a4f28c427f566c896f1cf67a697b3e40da988021f77edc9d5d303522ca3")
    version("1.5", sha256="a4474cf7cf4a507e80396712fa6be9df174e97d170536d05d6e5a3d7b2ec2a78")
    version("1.5.1", sha256="88379e149c382379dc16e148f9d51a05c4761bf3a3db9d4c2430b1bb94684955")
    version("1.5.2", sha256="c1dd17f558014fcedefaf55c1fbb9416c2391515f0718523db3ace47ac774d81")
    version("2.0", sha256="328aeedb0b5a0e907a7d94030d55c3c0795e24ae1a44efa07d054eb15aa17d5b")
    version("2.0.1", sha256="fb9084288d252b9dd11613167efa875b5da5db07c5a370b7f474a954be4b9ddc")
    version("2.1", sha256="4acd38e1311db45c9283d970c512415cb962112d68b253288d2018085cf4c697")
    version("2.1.1", sha256="ddd6fa8db87a04966df7bfcf05d3d04a4346db170f08f51b7fcdaf9ca985c06a")
    version(
        "2.10",
        sha256="f73e1176e8b7e9c9d38444f4894b80c84ecc7deb524828d78c70bf1e1df7bb80",
        expand=False,
        url="https://files.pythonhosted.org/packages/c4/7d/eeda1531b31e7479455ae32114fe17b1ef1ea8f4711224b4dd36be3bb3d1/visidata-2.10-py2.py3-none-any.whl",
    )
    version(
        "2.10.1",
        sha256="30ca9d65608a8f9d62798bda4a689c2b443ee042ddb59b76fa123ac814c2e899",
        expand=False,
        url="https://files.pythonhosted.org/packages/d0/e2/dfb2f2a436cda0f0f33dcd4582168010d2536948e90c4549d4b158952116/visidata-2.10.1-py3-none-any.whl",
    )
    version(
        "2.10.2",
        sha256="fe10c88f585e8e1c79a60a7e5dc08e1097d84c73d741a1fa10db0422252b6318",
        expand=False,
        url="https://files.pythonhosted.org/packages/92/b6/bab9e47a88c9ffb3505ee2e05d56330852f12d48d983850f2d401e92bdae/visidata-2.10.2-py3-none-any.whl",
    )
    version(
        "2.11",
        sha256="84fd9c31ff3bce07055bfe735d0455fca69db462db284c61b53e88e55debba77",
        expand=False,
        url="https://files.pythonhosted.org/packages/8c/a2/90b632ce4f9d11de1ab0600714bb57cc2aff662a47183111f55790f8f9b6/visidata-2.11-py3-none-any.whl",
    )
    version(
        "2.11.1",
        sha256="4e181a4938f469f08c71be325e3ea062eba7ceeead9708d6ced34a346ab1d3ac",
        expand=False,
        url="https://files.pythonhosted.org/packages/53/c3/cd217f9621e520fb29cb28ed153c994d25f1c2475c49640ee488a398a48d/visidata-2.11.1-py3-none-any.whl",
    )
    version(
        "2.11.dev0",
        sha256="d27bfb8fccb7fe228b75b61dcf0da83643bceb527fd4d63520c235b379ecca74",
        expand=False,
        url="https://files.pythonhosted.org/packages/64/65/d37c5f9b6ebe57ff9621f2d918d10b9baf5ad73db48cceb2ee5fbfc088ba/visidata-2.11.dev0-py3-none-any.whl",
    )
    version(
        "2.2",
        sha256="11c5848089b79a23e7c8c511daf62032015b03d1e6de5292b361fcae82397867",
        expand=False,
        url="https://files.pythonhosted.org/packages/c4/65/548b33547db81cd8bdabe0d9be493f1d644166a86e55d1f6a3a3e57d0e0b/visidata-2.2-py2.py3-none-any.whl",
    )
    version(
        "2.2.1",
        sha256="1d69dcdaaa6e954004017a75a7ddfa89a3a8944db05ff2b78666a3af992bbf1a",
        expand=False,
        url="https://files.pythonhosted.org/packages/01/b6/442621b254da9fac0ce43332f84c86b1b38a56ce7edf989ba74898ac0d1d/visidata-2.2.1-py2.py3-none-any.whl",
    )
    version(
        "2.3",
        sha256="4cb16c96d97cb9d86a13307e8d052ef5e64ab1ee3a86c5a8f8d5e2eba0913352",
        expand=False,
        url="https://files.pythonhosted.org/packages/83/7e/469a991f69c30b2cc132c61e0b30abb9a22f7bf36a92a0f7fc3bfe7c4c5f/visidata-2.3-py2.py3-none-any.whl",
    )
    version(
        "2.4",
        sha256="11a7e3f2813f76d745203752b6417c484094cdd7319aa25ff666b52c771f8ce3",
        expand=False,
        url="https://files.pythonhosted.org/packages/ac/a1/8ceea7ad26aefdfb844d2fe4f58b21362044897486308e2554a12836ffb8/visidata-2.4-py2.py3-none-any.whl",
    )
    version(
        "2.5",
        sha256="5142a27ec605e9ef616c46fee75d6e07e6a9e4a73fd0e4a5838fec332b6a7702",
        expand=False,
        url="https://files.pythonhosted.org/packages/78/89/23993b9757595405bfb3926b00920f8e89d297d1a2079bd51885fde799c0/visidata-2.5-py2.py3-none-any.whl",
    )
    version(
        "2.6",
        sha256="c48f67d9d891530b1c74ca135dc63578714ee9e83ae43b5d9f434fd6e8dcc17a",
        expand=False,
        url="https://files.pythonhosted.org/packages/4f/2f/2ebe404f7250f2e42c0db4f99b2d2a4595832ae5326b634c7962180b2fa6/visidata-2.6-py2.py3-none-any.whl",
    )
    version(
        "2.6.1",
        sha256="8aca3a2a1551a8e73a44f138378018635602b94dcffeea94ae101af2f1eca31c",
        expand=False,
        url="https://files.pythonhosted.org/packages/5a/0a/8fd72749c9f43efe0e7a8e6f648de3c225fb906e3b6911ed15cf5a95937d/visidata-2.6.1-py2.py3-none-any.whl",
    )
    version(
        "2.7",
        sha256="702f9ea9e577d54a6a09222f91ce0ef65b825020b5192e583f4b7786bf91a7ea",
        expand=False,
        url="https://files.pythonhosted.org/packages/1d/31/7be0a82718d8165946a434e92cd3be9c44f3d9efd9afb06aa9465eed0fd9/visidata-2.7-py2.py3-none-any.whl",
    )
    version(
        "2.7.1",
        sha256="16f8c46ee8000a3eb037b962d66b36e8de00f7a962c27808b701e4fe7fafbbc7",
        expand=False,
        url="https://files.pythonhosted.org/packages/1e/25/89cfab623f0409b92a915b868d527a593bd098e93de5cd7122c212cd8eca/visidata-2.7.1-py2.py3-none-any.whl",
    )
    version(
        "2.8",
        sha256="3ceced8b95700b4f75da301a9601123757ba5b8fe300fe5c2aec29722a2fdaaa",
        expand=False,
        url="https://files.pythonhosted.org/packages/12/1a/adc62b60b5a0bc58f2fd4fc8ab1fafdecdfc286f9276502e7450a36e88bb/visidata-2.8-py2.py3-none-any.whl",
    )
    version(
        "2.9",
        sha256="44b9d40055aeeabcbd06e44d372c93e57c186ec7364e97d5b71195a339e4efe5",
        expand=False,
        url="https://files.pythonhosted.org/packages/de/02/39206a092234751435cfc7e7d7b23991b6f60223faa0f6b4abe09f164b0b/visidata-2.9-py3-none-any.whl",
    )
    version(
        "2.9.1",
        sha256="a2451e26af598f2236fddec0da7f895ffecaa413b842ea35739d11809fc90a38",
        expand=False,
        url="https://files.pythonhosted.org/packages/a5/b0/fb96fa6bbc5715f62acfb2917752cd8129a27a88104dc41421ffd142f779/visidata-2.9.1-py2.py3-none-any.whl",
    )
    version(
        "3.0",
        sha256="ff5f4707b44d4d9626c245eeab4696763d24e6c9b3fa9f65bd049373d518091c",
        expand=False,
        url="https://files.pythonhosted.org/packages/3c/e1/2ba308b4f5e000b06ed81622c1d734fff5dfa5353a1f07561acdfbc2c394/visidata-3.0-py3-none-any.whl",
    )
    version(
        "3.0.1",
        sha256="b5f0110fb6021ad65063588828bd35d3834d626d45b487336eab1886497b2631",
        expand=False,
        url="https://files.pythonhosted.org/packages/c3/48/896b946bb8ddbcebd678a6cf784286275ebcfafb59bdb08af411b0f033bf/visidata-3.0.1-py3-none-any.whl",
    )
    version(
        "3.0.2",
        sha256="30275fcd90294ecdb0d024e24bd655b7787a2ca367d64ea181f15fb470f74c38",
        expand=False,
        url="https://files.pythonhosted.org/packages/84/12/afe992fdd2c7c41c13f1397f45366f4e2039e2bd5c0bb76108370c0d543e/visidata-3.0.2-py3-none-any.whl",
    )
    version(
        "3.1",
        sha256="0f8d1cc014c015f1c5b6a8b88a90f4581a074757442f6409b91f33dc34ec675e",
        expand=False,
        url="https://files.pythonhosted.org/packages/7d/32/202c4207b00f0fa32055da656fb2dae006658390bcdac635bb044c3b8dd7/visidata-3.1-py3-none-any.whl",
    )
    version(
        "3.1.1",
        sha256="903d8bff23df18c794499bee2a653bdeff3a48f899638656287c704ceca63e8b",
        expand=False,
        url="https://files.pythonhosted.org/packages/56/60/5026e693dbd4c38d2d13a697aa61846a6791bd6131e8a84c8aa61c0d5180/visidata-3.1.1-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python+readline@3.8:", type=("build", "run"))
    depends_on("py-importlib-metadata", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))


# {'python-dateutil': ['2.10', '2.10.1', '2.10.2', '2.11', '2.11.1', '2.11.dev0', '2.2', '2.2.1', '2.3', '2.4', '2.5', '2.6', '2.6.1', '2.7', '2.7.1', '2.8', '2.9', '2.9.1', '3.0', '3.0.1', '3.0.2', '3.1', '3.1.1'], 'importlib-metadata(>=3.6)': ['2.10', '2.10.1', '2.10.2', '2.11', '2.11.1', '2.11.dev0'], 'windows-curses;platform_system=="Windows"': ['2.10', '2.10.1', '2.10.2', '2.11', '2.11.1', '2.11.dev0', '2.9', '2.9.1'], 'importlib-metadata>=3.6': ['3.0', '3.0.1', '3.0.2', '3.1', '3.1.1'], 'windows-curses!=2.3.1;platform_system=="Windows"': ['3.0', '3.0.1', '3.0.2', '3.1', '3.1.1'], 'importlib-resources;python_version<"3.9"': ['3.0', '3.0.1', '3.0.2', '3.1', '3.1.1'], "Faker;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "h5py;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "odfpy;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "openpyxl;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "pandas;extra=='test'": ['3.0.2'], "pytest;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "tomli;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "tabulate;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "wcwidth;extra=='test'": ['3.0.2', '3.1', '3.1.1'], "brotli;extra=='test'": ['3.1', '3.1.1'], "dnslib;extra=='test'": ['3.1', '3.1.1'], "dpkt;extra=='test'": ['3.1', '3.1.1'], "fecfile;extra=='test'": ['3.1', '3.1.1'], "lxml;extra=='test'": ['3.1', '3.1.1'], "msgpack;extra=='test'": ['3.1', '3.1.1'], "pandas>=1.5.3;extra=='test'": ['3.1', '3.1.1'], "pyarrow;extra=='test'": ['3.1', '3.1.1'], "pyconll;extra=='test'": ['3.1', '3.1.1'], "pypng;extra=='test'": ['3.1', '3.1.1'], "PyYAML>=5.1;extra=='test'": ['3.1', '3.1.1'], "xport>=3.0;extra=='test'": ['3.1', '3.1.1']}

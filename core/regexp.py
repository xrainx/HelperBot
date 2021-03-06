# -*- coding: utf-8 -*-
# FIX: переделать строки в """
PROFILE = '(🇬🇵|🇮🇲|🇨🇾|🇻🇦|🇪🇺|🇲🇴|🇰🇮)(.+), (.+) .+ замка\n' \
          '🏅Уровень: ([0-9]+)\n' \
          '(?:.*)Атака: ([0-9]+) 🛡Защита: ([0-9]+)\n' \
          '🔥Опыт: ([0-9]+)/([0-9]+)\n' \
          '🔋Выносливость: ([0-9]+)/([0-9]+)\n' \
          '(?:💧Мана: [0-9]+/[0-9]+\n)?' \
          '💰(-?[0-9]+) 💠([0-9]+)\n\n' \
          '🎽Экипировка (.+)\n' \
          '🎒Рюкзак: ([0-9]+)/([0-9]+) /inv' \
          '(?:\n\nПомощник:\n(.+?) (?:.+?) (.+)? \(([0-9]+) ур\.\) (.+) /pet)?'

HERO = '(🇬🇵|🇮🇲|🇨🇾|🇻🇦|🇪🇺|🇲🇴|🇰🇮)(.+), (.+) .+ замка\n' \
       '🏅Уровень: ([0-9]+)\n' \
       '(?:.*)Атака: ([0-9]+) 🛡Защита: ([0-9]+)\n' \
       '🔥Опыт: ([0-9]+)/([0-9]+)\n' \
       '🔋Выносливость: ([0-9]+)/([0-9]+)\n' \
       '(?:💧Мана: [0-9]+/[0-9]+\n)?' \
       '💰(-?[0-9]+) 💠([0-9]+)\n' \
       '🤺Побед: ([0-9]+)\n\n' \
       '🎽Экипировка(?:(.+)(?:\n)?((?:.|\n)+)?)\n\n' \
       '🎒Рюкзак: ([0-9]+)/([0-9]+) /inv\n' \
       '📦Склад: (?:[0-9]+) /stock(?:\n\n' \
       'Помощник:\n' \
       '(.+?) (?:.+?) (.+)? \(([0-9]+) ур\.\) (.+) /pet)?'

REPORT = '(🇬🇵|🇮🇲|🇨🇾|🇻🇦|🇪🇺|🇲🇴|🇰🇮)(.+) ⚔️:([0-9]+) 🛡:([0-9]+) \(([0-9]+) ур.\)\n' \
       'Твои результаты в бою:(?:\n' \
       '🔥Опыт: ([0-9]+) ед)?(?:\n' \
       '💰Золото: (-?[0-9]+))?(?:\n' \
       '📦Склад: (-?[0-9]+))?'

BUILD_REPORT = 'Ты вернулся со стройки: (.+), прогресс работ: ([0-9]+)%'

REPAIR_REPORT = 'Здание отремонтировано: (.+)'

STOCK = '📦содержимое склада'

TRADE_BOT = '📦твой склад с материалами:'

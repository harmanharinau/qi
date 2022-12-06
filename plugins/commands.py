
                invite_link =  await c.create_chat_invite_link(int(db_channel))
            except Exception as e:
                return await m.reply_text("Make sure you you have made the bot as admin in ur channel "+str(db_channel))
                

            REPLY_MARKUP = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('Allow DB Channel', callback_data=f'dbgive_access#{group_id}#{m.from_user.id}#{db_channel}'),
            InlineKeyboardButton('Deny', callback_data=f'dbdeny_access#{m.from_user.id}#{db_channel}'),
        ],
        [
            
            InlineKeyboardButton('Close', callback_data=f'delete'),
        ],

    ])      

            await c.send_message(Config.LOG_CHANNEL,  f"Join the channel and then alllow. \n\n#NewDBChannel\n\nDB Chnl Invite Link: {invite_link.invite_link}\nGroup:`{group_id}`\n\nNote: This group has been already has access", reply_markup=REPLY_MARKUP)
            return await m.reply_text("Database Channel added successfully. Wait for the admin to approve the channel. You will be notified", )
        else:
            return await m.reply_text("Make the bot admin in the channel and /database -100xxx")
    else:
        return await m.reply_text("Your group does not have access to this command. Please /Verify access")
